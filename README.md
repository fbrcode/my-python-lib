# Build Python Library

## Initialize project

- `poetry new --name=lib .`
- `poetry config virtualenvs.in-project true --local`
- `git init`
- `poetry shell`
- `echo ".venv" >> .gitignore`
- `git add .`
- `git commit -m "initial lib project"`
