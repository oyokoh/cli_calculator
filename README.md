# CLI Calculator

A simple command-line calculator built with Python.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Modulo (remainder)
- Input validation
- Division-by-zero and modulo-by-zero handling

## Requirements

- Python 3
- No external dependencies

## Run the Calculator

```bash
python3 main.py
```

## Run the Tests

```bash
python3 -m unittest discover -s tests -v
```

## Project Structure

```text
cli_calculator/
├── calculator/
│   ├── __init__.py
│   └── operations.py
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_operations.py
├── main.py
├── README.md
└── .gitignore
```
