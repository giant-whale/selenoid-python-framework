# Python framework for Selenoid
This is a python PageObject framework for Selenoid hub, replacement of Selenium hub. 

Read more about Selenoid — https://aerokube.com/selenoid/
## Requirements
Python 3.8
## Installation
1. Follow this guide to install and run Selenoid — https://aerokube.com/selenoid/latest/
2. Download Docker images with browsers for Selenoid. If you want to use VNC option, you have to download VNC versions too;
3. Create new virtual environment and use package manager pip to install all requirements: ```pip install -r requirements.txt```
## Configuration
Before running tests, change `SELENOID_REMOTE_URL` variable in `core/settings.py` to your Selenoid address.
## Run your tests
Simply execute command `pytest tests/` to run all tests.
