# Contributing to Network Security Monitor

## Code of Conduct

All contributors are expected to adhere to our Code of Conduct. Please read it before participating.

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests
5. Submit a pull request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/network-security-monitor
cd network-security-monitor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt
```

## Coding Standards

- Follow PEP 8 style guide
- Use type hints
- Add docstrings for all functions/classes
- Maintain 80% test coverage minimum
- Use descriptive variable names

## Testing

```bash
# Run tests
pytest

# Check coverage
pytest --cov=security_monitor tests/
```

## Documentation

- Update docstrings using Google style
- Add comments for complex logic
- Update README.md for new features
- Include examples for new functionality

## Pull Request Process

1. Update documentation
2. Ensure CI passes
3. Squash commits

## Security Guidelines

- Never commit credentials
- Use secure random number generation
- Validate all inputs
- Log security-sensitive actions
- Handle errors gracefully

## Feature Requests

Open an issue with:
- Clear description
- Use case
- Expected behavior
- Implementation suggestions

## Bug Reports

Include:
- Python version
- OS/environment
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs
