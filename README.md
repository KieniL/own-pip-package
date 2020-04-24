# own-pip-package

## Installation for packaging
Use: pip install setuptools wheel tqdm twine

## Create a script
see helloworld skript

## Create a setup.py
see setup.py for this


## Compile package
run: python setup.py bdist_wheel


## Install package locally
pip install dist/<filename>.whl


## Upload to pypip

### Step 1
    Create pypirc: The Pypirc file stores the PyPi repository information. Create a file in the home directory
        for Windows :  C:\Users\UserName\.pypirc 
        for *nix :   ~/.pypirc 
    And add the following content to it. Replace javatechy with your username.

[distutils] 
index-servers=pypi
[pypi] 
repository = https://upload.pypi.org/legacy/ 
username =javatechy

### Step 2
use python -m twine upload dist/*

## Install package from pip
pip install <name in setup.py> e.g:
pip install helloworld-kienast