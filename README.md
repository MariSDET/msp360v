# MSP360 Test Automation Project
This project is a take-home assignment for msp360. 

## Overview
Project consists of two modules: API tests and UI tests.

API tests are written with pytest and use simple http helper functions to perform api calls, all relevant files are located in ```tests/api``` folder.

UI tests are written with pytest and playwright, all files are located in ```tests/playwright``` folder.

## Prerequisites

- Python 3.7+
- `pip` (Python package installer)

## Recommended Setup
It is recommended to use a virtual environment to manage dependencies and avoid conflicts with other projects. 

Project expects credentials and other information to be present in OS environment variables, recommended approach to provide it is to use ```.env``` file (see setup instructions).

## Setup Instructions

1. Clone the repository:

```sh
git clone https://github.com/MariSDET/msp360v
cd msp360v
```

2. Create a virtual environment:

```sh
python3 -m venv venv
```
3. Activate the virtual environment: 
```sh
source venv/bin/activate
```

4. Install the required packages:
```sh
pip install -r requirements.txt
```

5. Create .env file in the root folder of the project and put the following contents there:
```
API_USERNAME=<API USERNAME>
API_PASSWORD=<API PASSWORD>

USERNAME = <WEB UI USERNAME>
PASSWORD = <WEB UI PASSWORD>
BASE_URL = <WEB UI BASE URL>
BASE_URL_CONSOLE = <WEB UI BASE URL FOR CONSOLE>
PLAYWRIGHT_BROWSER_HEADLESS = <TRUE/FALSE> # depending on whether you want playwright browser to be running headless or not, default value is false
```

## Running Tests

To run the tests, use the following command:
```sh
python3 -m pytest -s tests
```
to run only API tests:
```sh
python3 -m pytest -s tests/api
```

to run only UI tests:
```sh
python3 -m pytest -s tests/playwright
```

Note: The -s option is used to disable output capturing, allowing you to see log messages and other outputs directly in the console.