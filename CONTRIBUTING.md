# Contributing

Thank you for considering contributing to HOLY-BIBLE!

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install the project in editable mode:
   ```bash
   pip install -e .
   ```

## Running Tests
Run all tests with:
```bash
python -m pytest
```

## Formatting
Use `black` for formatting and `flake8` (via `nbqa` for notebooks) for linting:
```bash
black .
flake8
nbqa flake8 old_testament/genesis/Genesis.ipynb
```

## Pull Requests
1. Fork the repository and create a feature branch.
2. Commit your changes with clear messages.
3. Ensure all tests pass and linting succeeds.
4. Open a pull request describing your changes.
