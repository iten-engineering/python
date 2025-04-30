# Development

Content
- [Package Manager](#package-manager)
- [Package Manager Scenarios](#package-manager-scenarios)
- [Commands](#commands)

# Package Manager

Python Package Managers Overview (2025):
Below is a summary of the most widely used Python package and environment managers.

## 1. pip
- **Description**: The standard package installer for Python.
- **Key Features**:
  - Installs from [PyPI](https://pypi.org/)
  - Supports `requirements.txt`
  - Compatible with `venv`, `virtualenv`
- **Command Example**: `pip install requests`

## 2. pipx
- **Description**: Installs and runs Python CLI tools in isolated environments.
- **Key Features**:
  - Each tool runs in its own virtual environment
  - Great for installing dev tools like `black`, `httpie`
- **Command Example**: `pipx install black`

## 3. conda
- **Description**: A powerful package and environment manager from Anaconda Inc.
- **Key Features**:
  - Manages both Python and non-Python dependencies (e.g., C, Fortran libraries)
  - Works across platforms
  - Strong isolation via environments
- **Command Example**: `conda install numpy`

## 4. Anaconda
- **Description**: A full Python/R distribution for data science, including `conda`.
- **Key Features**:
  - Pre-bundled with 250+ scientific packages
  - Includes `conda`, Jupyter, Spyder, and more
  - Heavyweight (3–4 GB)
  - Best for beginners in data science and ML
- **Website**: [anaconda.com](https://www.anaconda.com/)

## 5. Miniconda
- **Description**: A minimal installer for `conda`, without preinstalled packages.
- **Key Features**:
  - Lightweight alternative to Anaconda
  - Lets you install only what you need with `conda`
  - Recommended for advanced users or when storage is limited
- **Website**: [docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

## 6. poetry
- **Description**: Modern dependency and package manager using `pyproject.toml`.
- **Key Features**:
  - Manages dependencies and virtual environments
  - Simplifies publishing to PyPI
- **Command Example**: `poetry add requests`

## 7. pipenv
- **Description**: Combines `pip` and `virtualenv` for project management.
- **Key Features**:
  - Uses `Pipfile` and `Pipfile.lock`
  - Handles virtual environments automatically
  - Less active development in recent years
- **Command Example**: `pipenv install requests`

## 8. hatch
- **Description**: A modern tool focused on project, build, and environment management.
- **Key Features**:
  - Uses `pyproject.toml`
  - Plugin-based and fast
- **Command Example**: `hatch install`

## 9. flit
- **Description**: A lightweight tool for publishing pure Python packages.
- **Key Features**:
  - Uses `pyproject.toml`
  - Simple and fast
  - Great for libraries
- **Command Example**: `flit install`

## Comparison Table

| Tool       | Type                  | Virtual Env | `pyproject.toml` | Preinstalled Packages | CLI App Support | Conda Support |
|------------|-----------------------|-------------|------------------|------------------------|------------------|----------------|
| pip        | Installer              | ✅           | ❌ (manual only)  | ❌                      | ❌                | ❌              |
| pipx       | CLI App Installer      | ✅ (auto)    | ❌               | ❌                      | ✅                | ❌              |
| conda      | Env + Package Manager  | ✅           | ❌               | ❌                      | ❌                | ✅              |
| Anaconda   | Python Distribution    | ✅           | ❌               | ✅ (data science stack) | ❌                | ✅              |
| Miniconda  | Conda Installer        | ✅           | ❌               | ❌                      | ❌                | ✅              |
| poetry     | Project Manager        | ✅ (auto)    | ✅               | ❌                      | ❌                | ❌              |
| pipenv     | Project Manager        | ✅ (auto)    | ❌ (uses Pipfile) | ❌                      | ❌                | ❌              |
| hatch      | Project Manager        | ✅           | ✅               | ❌                      | ❌                | ❌              |
| flit       | Publisher Tool         | ❌           | ✅               | ❌                      | ❌                | ❌              |


# Package Manager Scenarios

Recommended Python Package Managers for Teams (Beginner → Expert)

| Scenario                          | Recommended Tool | Why                                                                 |
|----------------------------------|------------------|----------------------------------------------------------------------|
| Simple scripts or small tools    | `pip + venv`     | Built-in, easy to understand, no extra dependencies.                |
| CLI tools or dev utilities       | `pipx`           | Keeps tools isolated; perfect for formatters, linters, etc.         |
| Web/backend apps (general use)   | `poetry`         | Modern, beginner-friendly with good defaults, handles everything.   |
| Data science or ML projects      | `conda` or `Anaconda` | Handles Python + native libs easily, good IDEs included.        |
| Projects needing speed + plugins | `hatch`          | Fast, extensible, works well with `pyproject.toml`.                 |
| Lightweight packaging libraries  | `flit`           | Minimal setup for pure Python packages.                             |
| Full Anaconda stack, less setup  | `Anaconda`       | Ideal for teaching, all-in-one solution with notebooks & IDEs.      |
| Expert users with flexibility    | `Miniconda + poetry` | Combines light base + modern tooling.                           |

## Suggested Defaults for Most Teams

- 🟢 **Use `poetry`** for most application development — it's modern, team-friendly, and integrates with `pyproject.toml`.
- 🔵 **Use `conda`** (or `Anaconda`) for data-focused projects, especially if native dependencies are common.
- ⚙️ **Use `pipx`** alongside for managing dev tools like `black`, `flake8`, or `httpie`.


# Commands

## Conda

| Command                             | Description                     |
| ----------------------------------- | ------------------------------- | 
| conda --verson                      | Show version |
| conda info --envs                   | Show conda environments |
| conda list                          | Show installed libraries |
| conda install <package>             | Install a package |
| conda update <package>              | Update a package |
| conda create -n <env>               | Create conda environment |
| conda env create -f environment.yml | Create conda environment |
| conda env update -f environment.yml | Update conda environment |
| conda env remove -n <name>          | Remove conda environment |
| pip install <package>               | Install a package |
| pip update <package>                | Update a package |

> ! Execute command within the Anaconda Shell.


References:
- Conda
  https://conda.io

- User Guide
  https://conda.io/docs/user-guide/getting-started.html


## PIP

Package manager for Python packages (libraries). Packages are retrieved from a repository (Python package index): 

Command                              | Description
------------------------------------ | ---------------------------------------- 
pip --version                        | Show version
pip list                             | List all installed packages
pip install [packagename]            | Install package
pip install [packagename] == 2.1     | Install package with specific version
pip install –r [requirements.txt]    | Install packages from requirements file
pip install --upgrade [packagename]  | Updata package

References:
- PIP
  https://pypi.org/project/pip

- User Guide
  https://pip.pypa.io/en/stable/user_guide

- PIP Reference:
  https://pip.pypa.io/en/stable/reference/pip_list/

- Python package index
  https://pypi.org 
  
---
[Home](https://github.com/iten-engineering/python/blob/main/README.md) &nbsp; | &nbsp; [Top](#Development) &nbsp;
