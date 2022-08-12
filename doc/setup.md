# Setup

Content
- [Package Manager](#Package-Manager)
- [IDEs](#IDEs)
- [Troubleshoot](#Troubleshoot)


## Package Manager

### Anaconda

- Anaconda 
  - Offers a free Python distribution that includes the most important packages and tools for data science tasks 
  - Details see: https://www.anaconda.com

- Company with a typical open source-based business model: additional tools, support, consulting, training and cloud hosting 

- Anaconda Navigator
  - Manages Anaconda installation and included tools 
  - Installed together with Anaconde
  - Details see https://docs.anaconda.com/anaconda/navigator


### Conda

Package manager for Python (and other) packages (libraries):
- Packages are retrieved from a repository 
- Default and configurable repository 
- Supports multiple environments 
  - specific set of packages with specific versions 
  - configuration saved in environment.yaml 
  - can be shared between machines / developers 
  

Command                              | Description
------------------------------------ | ---------------------------------------- 
conda --version                      | Show version
conda info --envs                    | Show environments
conda create -n myenv phython=3.6.2  | Create environment with given phyton version
conda env remove -n myenv            | Remove environment
conda activate myenv                 | Activate the myenv environment
conda list                           | Show packages of active environment
conda install [pachagename]          | Install Package 
conda update [pachagename]           | Update Package 

> ! Execute command within the Anaconda Shell.


References:
- Conda
  https://conda.io

- User Guide
  https://conda.io/docs/user-guide/getting-started.html


### PIP

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
  

## IDEs

### Jupiter

Notebook-style IDE: 
- Web application that integrates code with text and interactive data visualizations
- Start 
  - Anaconda Navigator 
  - Command line: 
    `jupyter notebook --port [port]` 
  - Set working directory for notebooks:                    
    `jupyter notebook --notebook-dir='[path]'` 
- Runs on http://localhost:[port] 
  - See running servers: 
    `jupyter notebook list` 
  - incl. authentication token
- Create new Notebook via Web UI 
  - Navigate to desired location and click New -> Python3 notebook 
  - File saved as [name].ipynb 
  - Notebook page should open automatically in browser
- Stop notebook 
  - In the notebook page: click File -> Stop and Halt 
  - In the jupyter page: click Running and Shutdown 
- Stop server via killing the process 
  - Linux: 
    - `netstat –tulpn to retrieve pid`
    - `kill [pid]` 
  - Windows 
    - `netstat –ano` - to retrieve pid
    - `taskkill /PID [pid] /F`

References:

- Jupyter Notebook 
  https://jupyter.org

- Jupyter Notebook Documentation
  https://jupyter.org/documentation.html

- Installing Python Packages from a Jupyter Notebook:
  https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/


### Spyder

Classic IDE for Python (https://pythonhosted.org/spyder)

### PyCharme or IntelliJ Ultimate

JetBrains PyCharme or IntelliJ Ultimate
- https://www.jetbrains.com/pycharm 

### VS Code

Getting Started with Python in VS Code 
- https://code.visualstudio.com/docs/python/python-tutorial


## Troubleshoot

### IntelliJ

- Library im IntelliJ nicht `sichtbar`:
  - Falls Installation via IntelliJ oder Conda gemacht und Library immer noch nicht verfügbar: Installation mit `pip install <library>` versuchen
  
- Settings / Jupiter Notebook: Interpreter setzen


---
[Home](README.md) &nbsp; | &nbsp; [Top](#Setup) &nbsp;
