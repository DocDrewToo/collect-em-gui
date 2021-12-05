# Setup
* [One Time Setup](#pre-requisites-one-time-setup)
  * [Install Python](#python3)
  * [Application code](#application-setup)
  * [Pipenv - Python virtual env](#pipenv-python-virtual-environment)
* [Running the app locally](#running-locally)
---

## Pre-requisites / One time setup
### Install the following:  

1. **Python3**  
    Mac/Windows: https://www.python.org/downloads/

### Application setup:  

1. First, perform a git clone on this repo.  
    ``` shell
    git clone https://github.com/DocDrewToo/cis-553-python.git
    cd cis-553-python
    ```
1. **pipenv** - python virtual environment

    ```shell
    pip3 install --user pipenv
    ```
    > More info on Pipenv can be found here [pipenv](pipenv.pypa.io) and here [pipenv tutorial](https://realpython.com/pipenv-guide/)

1. Install the python dependencies inside the pipenv:  
    ```shell
    pipenv install
    ```

## Running the app Locally

1. Start the python virtual environment:  
    ```shell
    pipenv shell
    ```

1. Start the flask python application:  
    ```shell
    streamlit run pokelit.py
    ```
