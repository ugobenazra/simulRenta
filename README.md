# SimulRenta

SimulRenta is a Python application for simulating various rental scenarios using data-driven insights. The app is built with Python and uses `Poetry` for dependency management, as well as Docker for containerization.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Docker Setup](#docker-setup)
- [License](#license)

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


