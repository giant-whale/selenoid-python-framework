import time

import allure
import pytest
from selenium.webdriver import ChromeOptions

from core.browsers import (
    CHROME,
    FIREFOX,
)
from core.driver import Driver
from core.exceptions import DriverSetupException
from core.mobile_emulation import device_iphone8
from core.settings import SELENOID_REMOTE_URL


def pytest_addoption(parser):
    parser.addoption('--vnc', action='store_true', default=False)
    parser.addoption('--video', action='store_true', default=False)
    parser.addoption('--browser', action='store', default='chrome')


def is_mobile(request) -> bool:
    markers = request.node.own_markers
    if [mark for mark in markers if mark.name.lower() == 'mobile']:
        return True
    else:
        return False


@pytest.fixture(autouse=True)
def driver(request):
    with allure.step('Driver setup: parsing parameters'):
        mobile = is_mobile(request=request)

        browser = request.config.getoption('--browser')
        browser_capabilities = None

        if browser == 'chrome':
            chrome_options = ChromeOptions()
            if mobile:
                chrome_options.add_experimental_option('mobileEmulation', device_iphone8)
            browser_capabilities = chrome_options.to_capabilities()
            browser_capabilities['version'] = CHROME['browserVersion']

        elif browser == 'firefox':
            browser_capabilities = FIREFOX
            if mobile:
                raise DriverSetupException('Unable to use mobile emulation with Firefox - use Chrome instead')

        if request.config.getoption('--vnc'):
            browser_capabilities['enableVNC'] = True
        if request.config.getoption('--video'):
            browser_capabilities['enableVideo'] = True
        browser_capabilities['name'] = f'{browser}:{request.node.name}:{time.ctime()}'

    webdriver = Driver(command_executor=SELENOID_REMOTE_URL, desired_capabilities=browser_capabilities)
    webdriver.set_window_size(1920, 1080)

    yield webdriver

    with allure.step('Driver teardown'):
        try:
            webdriver.quit()
        finally:
            webdriver.__class__._instances = {}
