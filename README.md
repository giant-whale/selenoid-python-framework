# Python framework for Selenoid
This is a python PageObject framework for Selenoid hub, replacement of Selenium hub. 

Read more about Selenoid — https://aerokube.com/selenoid/

## Requirements
Python 3.11

## Installation
1. Follow this guide to install and run Selenoid — https://aerokube.com/selenoid/latest/
2. Download Docker images with browsers for Selenoid. If you want to use VNC option, you have to download VNC versions too;
3. Create new virtual environment and use package manager pip to install all requirements: ```pip install -r requirements.txt```;
4. Follow this guide to install Allure — https://docs.qameta.io/allure/#_get_started

## Configuration
Before running tests, change `SELENOID_REMOTE_URL` variable in `core/settings.py` to your Selenoid address.

## Browsers
List of available browsers in `core/browsers.py`. To add and use more browsers, check Selenoid documentation – https://aerokube.com/selenoid/latest/#_browser_images

## Mobile Emulation
Mobile emulation is available only for Google Chrome. 

Usage: add decorator `@pytest.mark.mobile` to your test on class to use mobile emulation. 

To add more mobile devices:
1. Add new mark to `pytest.ini`;
2. Add new devices in `core/mobile_emulation.py`;
3. Change `is_mobile` function in `conftest.py` — it requires new logic;
4. Add new branch for driver setup in `conftest.py`. 

## Run your tests
Multiple threads:
- Single-thread — execute command `pytest tests/` to run all tests in 1 thread;
- Multi-thread — execute command `pytest tests/ -n 5` to run all tests in 5 threads.

Select browser:
- Execute command `pytest tests/ --browser=chrome` to run all tests using Google Chrome. Also, it's declared as default browser, so there is no need to use this command — you can use `pytest tests/` instead;
- Execute command `pytest tests/ --browser=firefox` to run all tests using Mozilla Firefox;

Generate Allure report:
- Execute command `pytest tests/ --alluredir=./allure_results` to run all tests and generate Allure report files in directory `./allure_reports`. To run human-readable Allure report, execute command from the same directory `allure serve ./allure_results`.    
