import allure
import pytest
import time

from core.browsers import (
    CHROME,
    FIREFOX,
)
from core.driver import Driver
from core.settings import SELENOID_REMOTE_URL


def pytest_addoption(parser):
    parser.addoption('--vnc', action='store_true', default=False)
    parser.addoption('--video', action='store_true', default=False)
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture(autouse=True)
def driver(request):
    with allure.step('Driver setup: parsing parameters'):
        browser = request.config.getoption('--browser')
        browser_capabilities = None
        if browser == 'chrome':
            browser_capabilities = CHROME
        elif browser == 'firefox':
            browser_capabilities = FIREFOX

        if request.config.getoption('--vnc'):
            browser_capabilities['enableVNC'] = True
        if request.config.getoption('--video'):
            browser_capabilities['enableVideo'] = True
        browser_capabilities['name'] = f'{browser}:{request.node.name}:{time.ctime()}'

    webdriver = Driver(command_executor=SELENOID_REMOTE_URL, desired_capabilities=browser_capabilities)

    yield webdriver

    with allure.step('Driver teardown'):
        try:
            webdriver.quit()
        finally:
            webdriver.__class__._instances = {}
