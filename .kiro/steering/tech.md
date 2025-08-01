# Technology Stack

## Primary Languages
- **Python 3.8+**: Core analysis engine, pattern matching, CLI implementation
- **TypeScript/Node.js 16+**: Cross-platform compatibility, additional tooling
- **JavaScript**: Frontend components, HTML report generation

## Build System & Package Management
- **Python**: `pyproject.toml` (primary), `requirements.txt`, `setup.py`
- **Node.js**: `package.json`, supports npm/yarn/pnpm
- **Build Tools**: Python setuptools, Node.js native build

## Key Dependencies
- **Python**: regex processing, YAML/JSON parsing, file I/O utilities
- **TypeScript**: Jest for testing, ESLint/Prettier for code quality
- **Templates**: Handlebars for report generation

## Development Tools
- **Testing**: Jest (TypeScript), pytest (Python)
- **Linting**: ESLint, Prettier (TypeScript), flake8/black (Python)
- **Type Checking**: TypeScript compiler, Python type hints

## Common Commands

### Development
```bash
# Python development
pip install -e .
python -m pytest tests/
python -m flake8 src/

# TypeScript development  
npm install
npm test
npm run lint
npm run build
```

### Testing
```bash
# Run all tests
python scripts/test.py
npm test

# Run specific test categories
pytest tests/unit/
pytest tests/integration/
```

### Build & Distribution
```bash
# Python package
python setup.py sdist bdist_wheel
pip install dist/*.whl

# TypeScript build
npm run build
npm pack
```

## Platform Support
- **OS**: Windows, macOS, Linux
- **Environments**: GitHub Codespaces, local development
- **CI/CD**: GitHub Actions compatible