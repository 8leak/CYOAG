# CYOAG

Choose Your Own Adventure Game.

## Setup

1. Install [Poetry](https://python-poetry.org/docs/#installation).
2. Install dependencies:
   ```bash
   poetry install
   ```

## Running the game

Start the game with:

```bash
poetry run play
```

## Development commands

The project defines helper scripts in `pyproject.toml` that can be invoked via Poetry:

- `poetry run tidy` – format the codebase using Black, isort and Ruff.
- `poetry run tidy-check` – verify formatting and linting without making changes.


