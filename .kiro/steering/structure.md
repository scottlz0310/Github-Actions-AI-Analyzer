# Project Structure

## Directory Organization

### Core Source Code (`src/`)
- **`core/`**: Main analysis engine components
  - `analyzer.py`: Primary orchestration and API
  - `log_processor.py`: Log cleaning and preprocessing
  - `pattern_matcher.py`: Error pattern detection
  - `context_collector.py`: Workflow and repository context gathering
  - `ai_prompt_optimizer.py`: AI prompt generation and optimization

- **`patterns/`**: Error pattern definitions by category
  - `dependency_patterns.py`: Package and dependency issues
  - `permission_patterns.py`: File and execution permissions
  - `environment_patterns.py`: Environment setup problems
  - `network_patterns.py`: Network and connectivity issues
  - `syntax_patterns.py`: Configuration and syntax errors

- **`languages/`**: Language-specific analysis modules
  - `base.py`: Base language analyzer class
  - `python/`, `javascript/`, `java/`: Language-specific implementations
  - Each language dir contains: `patterns.py`, `context_parser.py`, `quick_fixes.py`

- **`parsers/`**: File and data parsing utilities
  - `workflow_parser.py`: GitHub Actions YAML parsing
  - `log_parser.py`: Log file structure analysis
  - `repository_parser.py`: Repository metadata extraction
  - `action_parser.py`: GitHub Actions marketplace analysis

- **`cli/`**: Command-line interface
  - `commands/`: Individual CLI commands (`analyze.py`, `validate.py`, `watch.py`)
  - `utils/`: CLI utilities (formatters, progress bars)

- **`types/`**: Type definitions and data structures
- **`utils/`**: Common utilities (file ops, string processing, logging)

### Data & Configuration (`data/`)
- **`error-database/`**: Known error patterns and solutions
- **`templates/`**: Output templates for reports and AI prompts

### Testing (`tests/`)
- **`unit/`**: Component-level tests mirroring `src/` structure
- **`integration/`**: End-to-end workflow tests
- **`fixtures/`**: Test data (sample logs, workflows, repositories)

### Documentation (`docs/`)
- **`api/`**: API reference documentation
- **`guides/`**: User guides and tutorials
- **`patterns/`**: Pattern definition documentation

### Scripts (`scripts/`)
- Build, test, and maintenance automation scripts

## File Naming Conventions
- Python files: `snake_case.py`
- TypeScript files: `camelCase.ts` or `kebab-case.ts`
- Configuration files: Standard names (`pyproject.toml`, `package.json`)
- Test files: `*.test.py` or `*.test.ts`

## Module Organization
- Each major component has its own directory with `__init__.py`
- Language-specific modules follow consistent structure
- Utilities are shared across components
- Types are centrally defined and exported

## Configuration Files
- **Root level**: `pyproject.toml`, `package.json`, `tsconfig.json`
- **Quality tools**: `.eslintrc.js`, `.prettierrc`, `jest.config.js`
- **Project docs**: `README.md`, `CHANGELOG.md`