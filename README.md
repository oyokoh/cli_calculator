
# CLI Calculator

A simple command-line calculator built with Python.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Modulo (remainder)
- Repeating menu until the user quits
- Input validation
- Division-by-zero protection
- Unit tests

## Requirements

- Python 3.10 or later
- No third-party packages required

## Run the calculator

```bash
python3 main.py
```

## Run the tests

```bash
python3 -m unittest discover -s tests -v
```

## Project structure

- `main.py`: user interface and program flow
- `calculator/operations.py`: arithmetic functions
- `tests/test_operations.py`: calculation tests
- `tests/test_cli.py`: command-line interaction tests
