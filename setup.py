#!/usr/bin/env python3
"""
ThoughtShield - AI Agent Security Framework
Setup configuration for PyPI distribution
"""

from setuptools import setup, find_packages
import os

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read version from thoughtshield/__init__.py
def get_version():
    with open(os.path.join("thoughtshield", "__init__.py"), "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"').strip("'")
    return "1.0.0"

setup(
    name="thoughtshield",
    version=get_version(),
    author="Digital Lobster & ThoughtShield Contributors",
    author_email="contact@thoughtshield.ai",
    description="Zero-Trust Security Framework for AI Automation Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thoughtshield-ai/thoughtshield",
    project_urls={
        "Homepage": "https://thoughtshield.ai",
        "Documentation": "https://docs.thoughtshield.ai",
        "Source": "https://github.com/thoughtshield-ai/thoughtshield",
        "Bug Tracker": "https://github.com/thoughtshield-ai/thoughtshield/issues",
        "Changelog": "https://github.com/thoughtshield-ai/thoughtshield/releases",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Framework :: FastAPI",
    ],
    packages=find_packages(include=["thoughtshield", "thoughtshield.*"]),
    package_data={
        "thoughtshield": ["config.yaml", "py.typed"],
    },
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0",
        "pydantic>=2.5.0",
        "pydantic-settings>=2.1.0",
        "cryptography>=41.0.0",
        "pyjwt>=2.8.0",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "google-cloud-aiplatform>=1.38.0",
        "google-auth>=2.23.0",
        "requests>=2.31.0",
        "aiohttp>=3.9.0",
        "sqlalchemy>=2.0.0",
        "redis>=5.0.0",
        "structlog>=23.2.0",
        "prometheus-client>=0.19.0",
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0.0",
        "click>=8.1.0",
        "rich>=13.7.0",
    ],
    extras_require={
        "dev": [
            "black>=23.11.0",
            "isort>=5.12.0",
            "flake8>=6.1.0",
            "mypy>=1.7.0",
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "bandit>=1.7.0",
            "sphinx>=7.2.0",
            "pre-commit>=3.5.0",
            "ipython>=8.17.0",
        ],
        "ml": [
            "numpy>=1.24.0",
            "pandas>=2.1.0",
            "scikit-learn>=1.3.0",
        ],
        "monitoring": [
            "opentelemetry-api>=1.21.0",
            "opentelemetry-sdk>=1.21.0",
            "opentelemetry-exporter-prometheus>=1.21.0",
        ],
        "database": [
            "pymongo>=4.5.0",
            "alembic>=1.12.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "thoughtshield=thoughtshield.cli:main",
            "thoughtshield-audit=thoughtshield.cli:audit",
            "thoughtshield-serve=thoughtshield.cli:serve",
        ],
    },
    keywords=[
        "security",
        "ai",
        "automation",
        "zero-trust",
        "audit",
        "monitoring",
        "fastapi",
        "machine-learning",
        "cybersecurity",
    ],
    license="MIT",
    platforms=["any"],
    zip_safe=False,
    include_package_data=True,
)