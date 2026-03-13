# ThoughtShield 商业配置快速指南

## 📋 文件清单

### 核心商业文档
1. **MONETIZATION.md** - 完整收益策略和商业模式
2. **commercial-config.yaml** - 商业配置模板
3. **thoughtshield/commercial.py** - 商业逻辑实现

### 集成到主README.md的内容
- 商业模式概述（开源核心+商业增值）
- 定价策略和收入预测
- 商业集成代码示例
- 合作伙伴计划
- 商业支持联系方式

## 🚀 快速开始商业部署

### 1. 配置支付网关
```bash
# 设置环境变量
export STRIPE_PUBLIC_KEY="pk_live_..."
export STRIPE_SECRET_KEY="sk_live_..."
export STRIPE_WEBHOOK_SECRET="whsec_..."

# 可选：中国支付
export ALIPAY_APP_ID="..."
export ALIPAY_PRIVATE_KEY="..."
export WECHAT_MCH_ID="..."
export WECHAT_API_KEY="..."
```

### 2. 初始化商业管理器
```python
from thoughtshield.commercial import get_commercial_manager, PlanTier

# 获取商业管理器
manager = get_commercial_manager()

# 创建测试订阅
subscription = manager.create_subscription(
    user_id="test_user_001",
    plan_tier=PlanTier.PROFESSIONAL
)

print(f"创建订阅: {subscription.subscription_id}")
print(f"计划: {subscription.plan.name}")
print(f"价格: ${subscription.plan.price}/月")
```

### 3. 处理支付
```python
# 模拟支付处理
payment = manager.process_payment(
    subscription_id=subscription.subscription_id,
    payment_provider="stripe",
    amount=subscription.plan.price
)

print(f"支付成功: {payment.payment_id}")
print(f"收据: {payment.receipt_url}")
```

### 4. 检查使用限制
```python
# 检查用户是否超出限制
checks = [
    ("agents", 5),      # 用户想创建5个agent
    ("requests", 5000), # 用户今天已使用5000次请求
    ("storage", 8),     # 用户使用了8GB存储
]

for feature, usage in checks:
    allowed = manager.check_limits(
        user_id="test_user_001",
        feature=feature,
        usage=usage
    )
    print(f"{feature}: {'允许' if allowed else '拒绝'} (使用量: {usage})")
```

## 💰 定价策略实施

### 四层定价模型
```python
from thoughtshield.commercial import PlanTier

# 定义各层级计划
PLANS = {
    PlanTier.COMMUNITY: {
        "price": 0,
        "name": "社区版",
        "description": "免费开源版本"
    },
    PlanTier.PROFESSIONAL: {
        "price": 99,
        "name": "专业版", 
        "description": "中小企业解决方案"
    },
    PlanTier.ENTERPRISE: {
        "price": 499,
        "name": "企业版",
        "description": "大型企业解决方案"
    },
    PlanTier.FLAGSHIP: {
        "price": "定制",
        "name": "旗舰版",
        "description": "定制化顶级解决方案"
    }
}
```

### 收入预测计算
```python
def calculate_revenue_projection(years=3):
    """计算收入预测"""
    projections = {
        "year_1": {
            "professional_users": 100,
            "enterprise_users": 20,
            "flagship_clients": 5
        },
        "year_2": {
            "professional_users": 300,
            "enterprise_users": 60, 
            "flagship_clients": 15
        },
        "year_3": {
            "professional_users": 1000,
            "enterprise_users": 200,
            "flagship_clients": 30
        }
    }
    
    results = {}
    for year, data in projections.items():
        revenue = (
            data["professional_users"] * 99 * 12 +
            data["enterprise_users"] * 499 * 12 +
            data["flagship_clients"] * 50000  # 平均$50,000/年
        )
        results[year] = revenue
    
    return results

# 计算预测
projections = calculate_revenue_projection()
for year, revenue in projections.items():
    print(f"{year}: ${revenue:,.2f}")
```

## 🤝 合作伙伴计划实施

### 合作伙伴配置
```yaml
# partners.yaml
partners:
  technology:
    commission_rate: 0.30
    requirements:
      - product_integration: true
      - joint_marketing: true
      - technical_collaboration: true
    payout_schedule: "monthly"
    
  channel:
    commission_rate: 0.20
    requirements:
      - sales_certification: true
      - customer_support: true
      - local_presence: true
    payout_schedule: "monthly"
    
  content:
    commission_rate: 0.50
    requirements:
      - quality_standards: true
      - official_certification: true
      - regular_updates: true
    payout_schedule: "per_course"
```

### 合作伙伴收益计算
```python
def calculate_partner_commission(revenue, partner_type):
    """计算合作伙伴佣金"""
    commission_rates = {
        "technology": 0.30,
        "channel": 0.20,
        "content": 0.50
    }
    
    rate = commission_rates.get(partner_type, 0)
    commission = revenue * rate
    
    return {
        "partner_type": partner_type,
        "revenue": revenue,
        "commission_rate": rate,
        "commission_amount": commission,
        "payout": commission * 0.85  # 扣除15%平台费
    }

# 示例计算
revenue = 10000  # $10,000收入
for partner_type in ["technology", "channel", "content"]:
    result = calculate_partner_commission(revenue, partner_type)
    print(f"{partner_type}: ${result['commission_amount']:.2f} 佣金")
```

## 🏆 贡献者奖励计划

### 奖励计算器
```python
class ContributorRewards:
    """贡献者奖励计算"""
    
    REWARD_RANGES = {
        "feature_development": (500, 5000),
        "bug_fix": (50, 500),
        "security_vulnerability": (100, 10000),
        "documentation": (20, 200),
        "tutorial_creation": (100, 1000),
        "translation": (50, 500),
        "community_management": (500, 2000),
        "technical_support": (30, 100),
        "security_research": (1000, 10000),
        "paper_publication": (500, 5000)
    }
    
    def calculate_reward(self, contribution_type, quality_score):
        """计算奖励金额"""
        if contribution_type not in self.REWARD_RANGES:
            return 0
        
        min_reward, max_reward = self.REWARD_RANGES[contribution_type]
        
        # 根据质量评分计算奖励
        reward = min_reward + (max_reward - min_reward) * (quality_score / 100)
        
        return round(reward, 2)
    
    def generate_reward_report(self, contributions):
        """生成奖励报告"""
        total_rewards = 0
        report = []
        
        for contrib in contributions:
            reward = self.calculate_reward(
                contrib["type"],
                contrib.get("quality_score", 75)
            )
            
            report.append({
                "contributor": contrib["name"],
                "type": contrib["type"],
                "description": contrib.get("description", ""),
                "reward": reward
            })
            
            total_rewards += reward
        
        return {
            "total_contributors": len(contributions),
            "total_rewards": total_rewards,
            "contributions": report
        }

# 使用示例
rewards_calculator = ContributorRewards()

contributions = [
    {"name": "Alice", "type": "feature_development", "quality_score": 90},
    {"name": "Bob", "type": "bug_fix", "quality_score": 80},
    {"name": "Charlie", "type": "documentation", "quality_score": 85}
]

report = rewards_calculator.generate_reward_report(contributions)
print(f"总奖励: ${report['total_rewards']:.2f}")
```

## 📊 财务监控

### 收入仪表板
```python
import datetime
from thoughtshield.commercial import get_commercial_manager

class RevenueDashboard:
    """收入监控仪表板"""
    
    def __init__(self):
        self.manager = get_commercial_manager()
    
    def get_daily_revenue(self, date=None):
        """获取每日收入"""
        if date is None:
            date = datetime.datetime.now()
        
        start = datetime.datetime(date.year, date.month, date.day)
        end = start + datetime.timedelta(days=1)
        
        report = self.manager.get_revenue_report(start, end)
        return report
    
    def get_monthly_revenue(self, year=None, month=None):
        """获取月度收入"""
        if year is None:
            year = datetime.datetime.now().year
        if month is None:
            month = datetime.datetime.now().month
        
        start = datetime.datetime(year, month, 1)
        if month == 12:
            end = datetime.datetime(year + 1, 1, 1)
        else:
            end = datetime.datetime(year, month + 1, 1)
        
        report = self.manager.get_revenue_report(start, end)
        return report
    
    def get_revenue_trend(self, days=30):
        """获取收入趋势"""
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=days)
        
        daily_revenues = []
        current_date = start_date
        
        while current_date < end_date:
            next_date = current_date + datetime.timedelta(days=1)
            report = self.get_daily_revenue(current_date)
            daily_revenues.append({
                "date": current_date.date(),
                "revenue": report["total_revenue"],
                "payments": report["payment_count"]
            })
            current_date = next_date
        
        return daily_revenues

# 使用示例
dashboard = RevenueDashboard()

# 获取今日收入
today = dashboard.get_daily_revenue()
print(f"今日收入: ${today['total_revenue']:.2f}")

# 获取本月收入
this_month = dashboard.get_monthly_revenue()
print(f"本月收入: ${this_month['total_revenue']:.2f}")

# 获取30天趋势
trend = dashboard.get_revenue_trend(30)
total_30days = sum(day["revenue"] for day in trend)
print(f"30天总收入: ${total_30days:.2f}")
```

## 🚀 部署检查清单

### 商业部署前检查
- [ ] 支付网关配置完成（Stripe/PayPal/支付宝/微信）
- [ ] 环境变量安全设置
- [ ] 订阅计划配置验证
- [ ] 合作伙伴协议模板准备
- [ ] 贡献者奖励政策公示
- [ ] 财务监控系统测试
- [ ] 法律合规审查完成
- [ ] 客户支持渠道建立

### 发布后监控
- [ ] 每日收入报告自动生成
- [ ] 合作伙伴佣金自动计算
- [ ] 贡献者奖励自动发放
- [ ] 使用限制实时监控
- [ ] 客户满意度跟踪
- [ ] 财务KPI仪表板

## 📞 支持与帮助

### 商业部署支持
- **技术咨询**: commercial-support@thoughtshield.ai
- **支付集成**: payment-integration@thoughtshield.ai
- **法律合规**: legal@thoughtshield.ai
- **财务咨询**: finance@thoughtshield.ai

### 紧急联系方式
- **商业紧急**: emergency-commercial@thoughtshield.ai
- **支付问题**: payment-emergency@thoughtshield.ai
- **安全漏洞**: security@thoughtshield.ai

---

**💡 提示：** 完整的商业配置文档请参考 `MONETIZATION.md` 和 `commercial-config.yaml`。

**🚀 祝您商业部署顺利！**