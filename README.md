# Python framework for Selenoid
This is a python PageObject framework for Selenoid hub, replacement of Selenium hub. 

Read more about Selenoid — https://aerokube.com/selenoid/
## Requirements
Python 3.8
## Installation
1. Follow this guide to install and run Selenoid — https://aerokube.com/selenoid/latest/
2. Download Docker images with browsers for Selenoid. If you want to use VNC option, you have to download VNC versions too;
3. Create new virtual environment and use package manager pip to install all requirements: ```pip install -r requirements.txt```;
4. Follow this guide to install Allure — https://docs.qameta.io/allure/#_get_started
## Configuration
Before running tests, change `SELENOID_REMOTE_URL` variable in `core/settings.py` to your Selenoid address.
## Run your tests
Multiple threads:
- Single-thread — execute command `pytest tests/` to run all tests in 1 thread;
- Multi-thread — execute command `pytest tests/ -n 5` to run all tests in 5 threads.


Generate Allure report:
- Execute command `pytest tests/ --alluredir=./allure_results` to run all tests and generate Allure report files in directory `./allure_reports`. To run human-readable Allure report, execute command from the same directory `allure my_allure_results/`.    