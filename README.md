# SimulRenta

SimulRenta is a Python application on streamlit for simulating various rental scenarios using data-driven insights. The app is built with Python and uses `Poetry` for dependency management, as well as Docker for containerization.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Docker Setup](#docker-setup)

---

## Requirements
- Python 3.9 (excluding 3.9.7 due to compatibility issues)
- Poetry for dependency management
- Docker (optional, for running the app in a container)

---

## Installation

### Step 1: Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/simulRenta.git
cd simulRenta
```

### Step 2: Install Poetry 
If you don't have poetry installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```


### Step 3: Install dependencies
Once Poetry is installed, use it to install the dependencies specified in the pyproject.toml and poetry.lock files:

```bash
poetry install
```

## Running the App
To run the application, run streamlit app using the following command:

```bash
poetry run streamlit run src/SimulRenta.py
```

Now you can type this url in your browser:
http://localhost:8501/


## Docker Setup
We put a Dockerfile inside this repo in order to config docker. Thanks to that, you can run the app while dockerising it.
First build the image:

```bash
docker build -t simulrenta . 
```

And then create the conntainer:
```bash
docker run -dp 8501:8501 simulrenta
```

Now you can type this url in your browser:
http://localhost:8501/
