"""
ThoughtShield - Zero-Trust Security Framework for AI Automation Systems

A production-ready security framework designed to protect AI automation systems
from malicious intent, unauthorized access, and operational risks.
"""

__version__ = "1.0.0"
__author__ = "Digital Lobster & ThoughtShield Contributors"
__email__ = "contact@thoughtshield.ai"
__license__ = "MIT"
__copyright__ = "Copyright 2026 ThoughtShield AI"

from thoughtshield.auditor import ThoughtShieldAuditor
from thoughtshield.verifier import GoogleSignatureVerifier, JWTVerifier, HMACVerifier
from thoughtshield.middleware import ThoughtShieldMiddleware
from thoughtshield.detector import ThreatDetector
from thoughtshield.dispatcher import ResponseEngine
from thoughtshield.config import ThoughtShieldConfig
from thoughtshield.exceptions import ThoughtShieldException, SecurityViolationException
from thoughtshield.models import ThoughtSignature, SecurityDecision, ThreatReport

__all__ = [
    # Core components
    "ThoughtShieldAuditor",
    "GoogleSignatureVerifier",
    "JWTVerifier",
    "HMACVerifier",
    "ThoughtShieldMiddleware",
    "ThreatDetector",
    "ResponseEngine",
    "ThoughtShieldConfig",
    
    # Models
    "ThoughtSignature",
    "SecurityDecision",
    "ThreatReport",
    
    # Exceptions
    "ThoughtShieldException",
    "SecurityViolationException",
    
    # Metadata
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
]

# Package metadata
PACKAGE_NAME = "thoughtshield"
PACKAGE_DESCRIPTION = "Zero-Trust Security Framework for AI Automation Systems"
PACKAGE_URL = "https://github.com/thoughtshield-ai/thoughtshield"
DOCUMENTATION_URL = "https://docs.thoughtshield.ai"

# Security compliance information
SECURITY_STANDARDS = [
    "NIST Cybersecurity Framework",
    "ISO 27001",
    "SOC 2",
    "GDPR",
    "CCPA",
]

# Performance targets
PERFORMANCE_TARGETS = {
    "response_time": "<15ms",
    "interception_accuracy": ">95%",
    "false_positive_rate": "<5%",
    "throughput": ">1000 req/sec",
    "availability": "99.9%",
}

def get_version() -> str:
    """Get the current version of ThoughtShield."""
    return __version__

def get_security_standards() -> list:
    """Get the list of supported security standards."""
    return SECURITY_STANDARDS.copy()

def get_performance_targets() -> dict:
    """Get the performance targets for ThoughtShield."""
    return PERFORMANCE_TARGETS.copy()

def about() -> str:
    """Get information about ThoughtShield."""
    return f"""
ThoughtShield v{__version__}
============================
{__copyright__}
License: {__license__}

Description: {PACKAGE_DESCRIPTION}

Website: {PACKAGE_URL}
Documentation: {DOCUMENTATION_URL}

Supported Security Standards:
{chr(10).join(f'  • {std}' for std in SECURITY_STANDARDS)}

Performance Targets:
{chr(10).join(f'  • {k}: {v}' for k, v in PERFORMANCE_TARGETS.items())}
"""

# Initialize logging configuration
import logging
from thoughtshield.utils import setup_logging

# Set up default logging
setup_logging()

# Create package logger
logger = logging.getLogger(__name__)
logger.info(f"ThoughtShield v{__version__} initialized")

# Export version info
version_info = tuple(map(int, __version__.split('.')))