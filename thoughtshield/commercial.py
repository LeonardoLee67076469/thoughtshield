"""
ThoughtShield 商业模块
处理订阅、支付、许可证等商业功能
"""

import json
import logging
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field, validator

logger = logging.getLogger(__name__)


class PlanTier(str, Enum):
    """订阅计划层级"""
    COMMUNITY = "community"
    PROFESSIONAL = "professional"
    ENTERPRISE = "enterprise"
    FLAGSHIP = "flagship"


class BillingCycle(str, Enum):
    """计费周期"""
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"
    LIFETIME = "lifetime"


class PaymentStatus(str, Enum):
    """支付状态"""
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    REFUNDED = "refunded"
    CANCELED = "canceled"


class SubscriptionStatus(str, Enum):
    """订阅状态"""
    ACTIVE = "active"
    TRIALING = "trialing"
    PAST_DUE = "past_due"
    CANCELED = "canceled"
    UNPAID = "unpaid"


class FeatureLimits(BaseModel):
    """功能限制"""
    agents: int = Field(default=3, description="最大Agent数量")
    requests_per_day: int = Field(default=1000, description="每日请求限制")
    storage_gb: int = Field(default=1, description="存储空间(GB)")
    concurrent_tasks: int = Field(default=5, description="并发任务数")
    api_rate_limit: int = Field(default=100, description="API速率限制(每分钟)")
    
    @validator('agents', 'requests_per_day', 'storage_gb', 'concurrent_tasks', 'api_rate_limit')
    def validate_positive(cls, v):
        if v < 0:
            raise ValueError("限制值必须为正数")
        return v


class PlanFeatures(BaseModel):
    """计划功能"""
    basic_security: bool = Field(default=True, description="基础安全防护")
    advanced_threat_detection: bool = Field(default=False, description="高级威胁检测")
    team_collaboration: bool = Field(default=False, description="团队协作工具")
    custom_policies: bool = Field(default=False, description="自定义安全策略")
    dedicated_support: bool = Field(default=False, description="专属支持")
    sla_guarantee: bool = Field(default=False, description="SLA保证")
    compliance_certification: bool = Field(default=False, description="合规认证支持")
    source_code_access: bool = Field(default=False, description="源代码访问")
    white_label: bool = Field(default=False, description="白标解决方案")


class SubscriptionPlan(BaseModel):
    """订阅计划"""
    tier: PlanTier
    name: str
    description: str
    price: float
    currency: str = "USD"
    billing_cycle: BillingCycle = BillingCycle.MONTHLY
    features: PlanFeatures
    limits: FeatureLimits
    trial_days: int = 0
    is_active: bool = True
    
    @validator('price')
    def validate_price(cls, v):
        if v < 0:
            raise ValueError("价格不能为负数")
        return v
    
    @validator('trial_days')
    def validate_trial_days(cls, v):
        if v < 0 or v > 365:
            raise ValueError("试用期必须在0-365天之间")
        return v


class PaymentDetails(BaseModel):
    """支付详情"""
    payment_id: str
    provider: str  # stripe, paypal, alipay, wechat
    amount: float
    currency: str
    status: PaymentStatus
    created_at: datetime
    paid_at: Optional[datetime] = None
    receipt_url: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Subscription(BaseModel):
    """用户订阅"""
    subscription_id: str
    user_id: str
    plan: SubscriptionPlan
    status: SubscriptionStatus
    current_period_start: datetime
    current_period_end: datetime
    trial_start: Optional[datetime] = None
    trial_end: Optional[datetime] = None
    cancel_at_period_end: bool = False
    canceled_at: Optional[datetime] = None
    payment_details: Optional[PaymentDetails] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    @property
    def is_active(self) -> bool:
        """检查订阅是否活跃"""
        now = datetime.now()
        if self.status != SubscriptionStatus.ACTIVE:
            return False
        if now > self.current_period_end:
            return False
        return True
    
    @property
    def is_trialing(self) -> bool:
        """检查是否在试用期"""
        if not self.trial_end:
            return False
        now = datetime.now()
        return self.trial_start <= now <= self.trial_end
    
    @property
    def days_remaining(self) -> int:
        """剩余天数"""
        now = datetime.now()
        if self.is_trialing and self.trial_end:
            end_date = self.trial_end
        else:
            end_date = self.current_period_end
        
        remaining = (end_date - now).days
        return max(0, remaining)


class CommercialManager:
    """商业管理器"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.plans = self._load_plans()
        self.subscriptions: Dict[str, Subscription] = {}
        self.payments: Dict[str, PaymentDetails] = {}
        
    def _load_plans(self) -> Dict[PlanTier, SubscriptionPlan]:
        """加载预定义计划"""
        return {
            PlanTier.COMMUNITY: SubscriptionPlan(
                tier=PlanTier.COMMUNITY,
                name="社区版",
                description="免费开源版本，适合个人和小团队",
                price=0.0,
                features=PlanFeatures(
                    basic_security=True,
                    advanced_threat_detection=False,
                    team_collaboration=False,
                    custom_policies=False,
                    dedicated_support=False,
                    sla_guarantee=False,
                    compliance_certification=False,
                    source_code_access=False,
                    white_label=False
                ),
                limits=FeatureLimits(
                    agents=3,
                    requests_per_day=1000,
                    storage_gb=1,
                    concurrent_tasks=5,
                    api_rate_limit=100
                ),
                trial_days=0
            ),
            PlanTier.PROFESSIONAL: SubscriptionPlan(
                tier=PlanTier.PROFESSIONAL,
                name="专业版",
                description="适合中小企业的专业安全解决方案",
                price=99.0,
                billing_cycle=BillingCycle.MONTHLY,
                features=PlanFeatures(
                    basic_security=True,
                    advanced_threat_detection=True,
                    team_collaboration=True,
                    custom_policies=False,
                    dedicated_support=False,
                    sla_guarantee=True,
                    compliance_certification=False,
                    source_code_access=False,
                    white_label=False
                ),
                limits=FeatureLimits(
                    agents=10,
                    requests_per_day=10000,
                    storage_gb=10,
                    concurrent_tasks=20,
                    api_rate_limit=500
                ),
                trial_days=14
            ),
            PlanTier.ENTERPRISE: SubscriptionPlan(
                tier=PlanTier.ENTERPRISE,
                name="企业版",
                description="适合大型企业的全面安全解决方案",
                price=499.0,
                billing_cycle=BillingCycle.MONTHLY,
                features=PlanFeatures(
                    basic_security=True,
                    advanced_threat_detection=True,
                    team_collaboration=True,
                    custom_policies=True,
                    dedicated_support=True,
                    sla_guarantee=True,
                    compliance_certification=True,
                    source_code_access=False,
                    white_label=False
                ),
                limits=FeatureLimits(
                    agents=100,
                    requests_per_day=100000,
                    storage_gb=100,
                    concurrent_tasks=100,
                    api_rate_limit=5000
                ),
                trial_days=30
            ),
            PlanTier.FLAGSHIP: SubscriptionPlan(
                tier=PlanTier.FLAGSHIP,
                name="旗舰版",
                description="定制化的顶级安全解决方案",
                price=0.0,  # 定制价格
                billing_cycle=BillingCycle.YEARLY,
                features=PlanFeatures(
                    basic_security=True,
                    advanced_threat_detection=True,
                    team_collaboration=True,
                    custom_policies=True,
                    dedicated_support=True,
                    sla_guarantee=True,
                    compliance_certification=True,
                    source_code_access=True,
                    white_label=True
                ),
                limits=FeatureLimits(
                    agents=1000,
                    requests_per_day=1000000,
                    storage_gb=1000,
                    concurrent_tasks=500,
                    api_rate_limit=50000
                ),
                trial_days=60
            )
        }
    
    def create_subscription(
        self,
        user_id: str,
        plan_tier: PlanTier,
        payment_details: Optional[PaymentDetails] = None
    ) -> Subscription:
        """创建新订阅"""
        if plan_tier not in self.plans:
            raise ValueError(f"无效的计划层级: {plan_tier}")
        
        plan = self.plans[plan_tier]
        now = datetime.now()
        
        # 计算周期结束时间
        if plan.billing_cycle == BillingCycle.MONTHLY:
            period_end = now + timedelta(days=30)
        elif plan.billing_cycle == BillingCycle.QUARTERLY:
            period_end = now + timedelta(days=90)
        elif plan.billing_cycle == BillingCycle.YEARLY:
            period_end = now + timedelta(days=365)
        else:  # LIFETIME
            period_end = now + timedelta(days=36500)  # 100年
        
        # 设置试用期
        trial_start = None
        trial_end = None
        if plan.trial_days > 0:
            trial_start = now
            trial_end = now + timedelta(days=plan.trial_days)
        
        # 确定初始状态
        if plan.price == 0:
            status = SubscriptionStatus.ACTIVE
        elif plan.trial_days > 0:
            status = SubscriptionStatus.TRIALING
        else:
            status = SubscriptionStatus.PENDING
        
        subscription = Subscription(
            subscription_id=f"sub_{user_id}_{int(now.timestamp())}",
            user_id=user_id,
            plan=plan,
            status=status,
            current_period_start=now,
            current_period_end=period_end,
            trial_start=trial_start,
            trial_end=trial_end,
            payment_details=payment_details
        )
        
        self.subscriptions[subscription.subscription_id] = subscription
        logger.info(f"创建订阅: {subscription.subscription_id} for user {user_id}")
        
        return subscription
    
    def upgrade_subscription(
        self,
        subscription_id: str,
        new_plan_tier: PlanTier
    ) -> Subscription:
        """升级订阅"""
        if subscription_id not in self.subscriptions:
            raise ValueError(f"订阅不存在: {subscription_id}")
        
        subscription = self.subscriptions[subscription_id]
        new_plan = self.plans[new_plan_tier]
        
        # 检查是否允许升级
        if new_plan.price < subscription.plan.price:
            raise ValueError("只能升级到更高层级的计划")
        
        # 更新订阅
        subscription.plan = new_plan
        subscription.updated_at = datetime.now()
        
        logger.info(f"升级订阅 {subscription_id} 到 {new_plan_tier}")
        return subscription
    
    def cancel_subscription(
        self,
        subscription_id: str,
        cancel_at_period_end: bool = True
    ) -> Subscription:
        """取消订阅"""
        if subscription_id not in self.subscriptions:
            raise ValueError(f"订阅不存在: {subscription_id}")
        
        subscription = self.subscriptions[subscription_id]
        
        if cancel_at_period_end:
            subscription.cancel_at_period_end = True
            subscription.status = SubscriptionStatus.ACTIVE
        else:
            subscription.status = SubscriptionStatus.CANCELED
            subscription.canceled_at = datetime.now()
        
        subscription.updated_at = datetime.now()
        logger.info(f"取消订阅: {subscription_id}")
        
        return subscription
    
    def process_payment(
        self,
        subscription_id: str,
        payment_provider: str,
        amount: float,
        currency: str = "USD"
    ) -> PaymentDetails:
        """处理支付"""
        if subscription_id not in self.subscriptions:
            raise ValueError(f"订阅不存在: {subscription_id}")
        
        subscription = self.subscriptions[subscription_id]
        
        # 模拟支付处理
        payment_id = f"pay_{int(datetime.now().timestamp())}"
        payment = PaymentDetails(
            payment_id=payment_id,
            provider=payment_provider,
            amount=amount,
            currency=currency,
            status=PaymentStatus.SUCCEEDED,
            created_at=datetime.now(),
            paid_at=datetime.now(),
            receipt_url=f"https://receipt.thoughtshield.ai/{payment_id}"
        )
        
        # 更新订阅状态
        subscription.payment_details = payment
        subscription.status = SubscriptionStatus.ACTIVE
        subscription.updated_at = datetime.now()
        
        self.payments[payment_id] = payment
        logger.info(f"处理支付: {payment_id} for subscription {subscription_id}")
        
        return payment
    
    def check_limits(
        self,
        user_id: str,
        feature: str,
        usage: int = 1
    ) -> bool:
        """检查用户是否超出限制"""
        # 查找用户的活跃订阅
        user_subscriptions = [
            sub for sub in self.subscriptions.values()
            if sub.user_id == user_id and sub.is_active
        ]
        
        if not user_subscriptions:
            # 默认使用社区版限制
            plan = self.plans[PlanTier.COMMUNITY]
        else:
            # 使用最高层级的订阅
            user_subscriptions.sort(key=lambda x: x.plan.price, reverse=True)
            plan = user_subscriptions[0].plan
        
        # 检查具体限制
        if feature == "agents":
            return usage <= plan.limits.agents
        elif feature == "requests":
            return usage <= plan.limits.requests_per_day
        elif feature == "storage":
            return usage <= plan.limits.storage_gb
        elif feature == "concurrent_tasks":
            return usage <= plan.limits.concurrent_tasks
        elif feature == "api_rate":
            return usage <= plan.limits.api_rate_limit
        
        return True
    
    def get_user_plan(self, user_id: str) -> Optional[SubscriptionPlan]:
        """获取用户当前计划"""
        user_subscriptions = [
            sub for sub in self.subscriptions.values()
            if sub.user_id == user_id and sub.is_active
        ]
        
        if not user_subscriptions:
            return self.plans[PlanTier.COMMUNITY]
        
        user_subscriptions.sort(key=lambda x: x.plan.price, reverse=True)
        return user_subscriptions[0].plan
    
    def generate_invoice(
        self,
        subscription_id: str,
        period_start: datetime,
        period_end: datetime
    ) -> Dict[str, Any]:
        """生成发票"""
        if subscription_id not in self.subscriptions:
            raise ValueError(f"订阅不存在: {subscription_id}")
        
        subscription = self.subscriptions[subscription_id]
        plan = subscription.plan
        
        invoice = {
            "invoice_id": f"inv_{int(datetime.now().timestamp())}",
            "subscription_id": subscription_id,
            "user_id": subscription.user_id,
            "plan_name": plan.name,
            "amount": plan.price,
            "currency": plan.currency,
            "billing_cycle": plan.billing_cycle,
            "period_start": period_start.isoformat(),
            "period_end": period_end.isoformat(),
            "items": [
                {
                    "description": f"{plan.name} 订阅",
                    "amount": plan.price,
                    "quantity": 1
                }
            ],
            "total": plan.price,
            "status": "generated",
            "created_at": datetime.now().isoformat()
        }
        
        return invoice
    
    def get_revenue_report(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> Dict[str, Any]:
        """获取收入报告"""
        relevant_payments = [
            payment for payment in self.payments.values()
            if start_date <= payment.created_at <= end_date
            and payment.status == PaymentStatus.SUCCEEDED
        ]
        
        total_revenue = sum(p.amount for p in relevant_payments)
        
        # 按货币分组
        revenue_by_currency = {}
        for payment in relevant_payments:
            currency = payment.currency
            revenue_by_currency[currency] = revenue_by_currency.get(currency, 0) + payment.amount
        
        # 按支付提供商分组
        revenue_by_provider = {}
        for payment in relevant_payments:
            provider = payment.provider
            revenue_by_provider[provider] = revenue_by_provider.get(provider, 0) + payment.amount
        
        return {
            "period": {
                "start": start_date.isoformat(),
                "end": end_date.isoformat()
            },
            "total_revenue": total_revenue,
            "payment_count": len(relevant_payments),
            "revenue_by_currency": revenue_by_currency,
            "revenue_by_provider": revenue_by_provider,
            "average_payment_amount": total_revenue / len(relevant_payments) if relevant_payments else 0
        }


# 单例实例
_commercial_manager = None

def get_commercial_manager() -> CommercialManager:
    """获取商业管理器单例"""
    global _commercial_manager
    if _commercial_manager is None:
        _com