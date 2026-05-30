# AlgoTrading Repository

## Overview

This repository contains algorithmic trading bots and strategies.

## Development Guidelines

### Commit Messages

All commit messages must follow the Conventional Commits specification:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `build`: Changes that affect the build system or external dependencies
- `ci`: Changes to CI configuration files and scripts
- `chore`: Other changes that don't modify src or test files
- `revert`: Reverts a previous commit

**Examples:**
- `feat(auth): add JWT token validation`
- `fix(trading): resolve race condition in order execution`
- `docs: update API documentation`
- `refactor(db): optimize connection pooling`

### Pull Requests

PRs should have:
1. A descriptive title following conventional commits format
2. A detailed description explaining:
   - What changes were made
   - Why these changes were made
   - Any breaking changes or migration notes

### Code Style

- Follow PEP 8 for Python code
- Use type hints where applicable
- Write docstrings for public functions and classes
- Keep functions focused and small

### Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for meaningful test coverage, not just high numbers

## Project Structure

```
algotrading/
├── src/           # Source code
├── tests/         # Test files
├── config/        # Configuration files
├── docs/          # Documentation
└── scripts/       # Utility scripts
```

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables (see `.env.example`)
4. Run tests: `pytest`

## License

[Your License Here]
