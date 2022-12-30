# Build Python Library

## Initialize project

- `poetry new --name=lib .`
- `poetry config virtualenvs.in-project true --local`
- `git init`
- `poetry shell`
- `echo ".venv" >> .gitignore`
- `git add .`
- `git commit -m "initial lib project"`

## Add library code and test

- `touch lib/lib_functions.py`
- `poetry add pytest -D`
- `touch tests/test_lib_functions.py`
- `echo ".pytest_cache" >> .gitignore`
- `echo "__pycache__" >> .gitignore`
- `poetry run pytest`

## Packaging options

### poetry to build the library

- `poetry build`
- `echo "dist" >> .gitignore`

Use the `./dist/lib-0.1.0-py3-none-any.whl` file to install the library.
