# Python framework for Selenoid

## Requirements
Python 3.8 — https://www.python.org/downloads/

## Installation
1. Install python 3.8
2. Create new virtual environment (https://docs.python.org/3/library/venv.html) and use package manager pip to install all requirements: pip install -r requirements.txt;
3. Install Google Chrome webdriver — https://chromedriver.chromium.org/getting-started 
4. Follow this guide to install Allure (required to generate reports) — https://docs.qameta.io/allure/#_get_started

## Configuration
Before running tests, change `WEBDRIVER_LOCAL_PATH` variable in `core/settings.py` to your webdriver executable path.

## Mobile Emulation
Mobile emulation is available only for Google Chrome. 

Usage: add decorator `@pytest.mark.mobile` to your test to use mobile emulation. 

To add more mobile devices:
1. Add new mark to `pytest.ini`;
2. Add new devices in `core/mobile_emulation.py`;
3. Change `is_mobile` function in `conftest.py` — it requires new logic;
4. Add new branch for driver setup in `conftest.py`. 

## Run your tests
Multiple threads:
- Single-thread — execute command `pytest tests/` to run all tests in 1 thread;
- Multi-thread — execute command `pytest tests/ -n 5` to run all tests in 5 threads.

Generate Allure report:
- Execute command `pytest tests/ --alluredir=./allure_results` to run all tests and generate Allure report files in directory `./allure_reports`. To run human-readable Allure report, execute command from the same directory `allure allure_results/`.    
