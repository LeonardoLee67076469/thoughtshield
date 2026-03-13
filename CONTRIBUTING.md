# Contributing to ThoughtShield

🎉 **First, thank you for considering contributing to ThoughtShield!** 🎉

We're excited to have you join our community of AI security enthusiasts, researchers, and developers. This document provides guidelines and instructions for contributing to the ThoughtShield project.

## 🎯 Our Philosophy

ThoughtShield is built on three core principles:

1. **Security First**: Every contribution must prioritize security and user protection
2. **Community Driven**: We believe in collaborative development and shared ownership
3. **Practical Innovation**: We value solutions that solve real-world problems

## 📋 How to Contribute

### 1. Reporting Issues
Found a bug or have a feature request? Here's how to report it:

#### Bug Reports
```markdown
**Description**: Clear and concise description of the bug
**Steps to Reproduce**:
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

**Expected Behavior**: What you expected to happen
**Actual Behavior**: What actually happened
**Screenshots**: If applicable, add screenshots
**Environment**:
- OS: [e.g., macOS, Windows, Linux]
- Python Version: [e.g., 3.9, 3.10]
- ThoughtShield Version: [e.g., 1.0.0]
- OpenClaw Version: [if applicable]

**Additional Context**: Any other context about the problem
```

#### Feature Requests
```markdown
**Problem Statement**: What problem are you trying to solve?
**Proposed Solution**: How do you think we should solve it?
**Alternatives Considered**: What other solutions did you consider?
**Additional Context**: Any other information that might help
```

### 2. Code Contributions

#### Development Workflow
1. **Fork the Repository**: Click the "Fork" button on GitHub
2. **Clone Your Fork**: `git clone https://github.com/YOUR_USERNAME/thoughtshield.git`
3. **Create a Branch**: `git checkout -b feature/your-feature-name`
4. **Make Your Changes**: Follow our coding standards
5. **Test Your Changes**: Run the test suite
6. **Commit Your Changes**: Use descriptive commit messages
7. **Push to Your Fork**: `git push origin feature/your-feature-name`
8. **Open a Pull Request**: From your fork to our main repository

#### Coding Standards
- **Python**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- **Documentation**: Include docstrings for all public functions
- **Tests**: Write tests for new functionality
- **Type Hints**: Use Python type hints where applicable

### 3. Documentation Contributions
We need help with:
- **API Documentation**: Improving function and class documentation
- **Tutorials**: Step-by-step guides for common use cases
- **Translation**: Help translate documentation to other languages
- **Examples**: Create practical examples and demos

### 4. Security Research
If you're a security researcher:
- **Responsible Disclosure**: Email security@thoughtshield.ai
- **Attack Vectors**: Help expand our attack vector catalog
- **Penetration Testing**: Test ThoughtShield's defenses
- **Research Papers**: Contribute to our security research

## 🛠️ Development Setup

### Prerequisites
- Python 3.9+
- Git
- Virtual environment tool (venv, conda, etc.)

### Setup Instructions
```bash
# 1. Clone the repository
git clone https://github.com/thoughtshield-ai/thoughtshield.git
cd thoughtshield

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies

# 4. Install pre-commit hooks
pre-commit install

# 5. Run tests
pytest tests/ -v
```

### Development Tools
- **Code Formatting**: `black thoughtshield/`
- **Linting**: `flake8 thoughtshield/`
- **Type Checking**: `mypy thoughtshield/`
- **Testing**: `pytest tests/ -v`
- **Security Scanning**: `bandit -r thoughtshield/`

## 📝 Pull Request Guidelines

### Before Submitting
1. **Run Tests**: Ensure all tests pass
2. **Check Code Style**: Run black and flake8
3. **Update Documentation**: Update relevant documentation
4. **Add Tests**: Include tests for new functionality
5. **Check Security**: Ensure no security vulnerabilities

### PR Description Template
```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update
- [ ] Security fix

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing performed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] Security considerations addressed
- [ ] No breaking changes (unless intentional)

## Related Issues
Closes #123, Fixes #456
```

## 🏆 Recognition

We recognize contributors in several ways:

1. **Contributor Hall of Fame**: Featured in our README
2. **Release Notes**: Mentioned in release announcements
3. **Community Awards**: Special recognition for significant contributions
4. **Maintainer Status**: Active contributors may become maintainers

## 📚 Learning Resources

### For New Contributors
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Python Best Practices](https://docs.python-guide.org/)
- [Open Source Contribution Guide](https://opensource.guide/how-to-contribute/)

### ThoughtShield Specific
- [Architecture Overview](docs/architecture.md)
- [Security Model](docs/security-model.md)
- [API Reference](docs/api-reference.md)

## ❓ Need Help?

- **GitHub Discussions**: For questions and discussions
- **Discord**: Join our community chat
- **Email**: contributors@thoughtshield.ai
- **Office Hours**: Weekly contributor calls (check Discord for schedule)

## 📄 License

By contributing to ThoughtShield, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for helping make AI automation safer for everyone!** 🛡️

> "Security is not a product, but a process.  
> It's not about building walls, but about building trust.  
> And trust is built one contribution at a time."  
> — Digital Lobster 🦞