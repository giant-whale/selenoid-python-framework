import time

import allure
import pytest
from selenium.webdriver import ChromeOptions

from core.browsers import (
    CHROME,
)
from core.driver import Driver
from core.exceptions import DriverSetupException
from core.mobile_emulation import device_iphone8
from core.settings import WEBDRIVER_LOCAL_PATH


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

        browser = 'chrome'
        browser_capabilities = None

        if browser == 'chrome':
            chrome_options = ChromeOptions()
            if mobile:
                chrome_options.add_experimental_option('mobileEmulation', device_iphone8)
            browser_capabilities = chrome_options.to_capabilities()
            browser_capabilities['version'] = CHROME['browserVersion']
        else:
            raise DriverSetupException(f'Unsupported browser — {browser}')

        browser_capabilities['name'] = f'{browser}:{request.node.name}:{time.ctime()}'

    webdriver = Driver(executable_path=WEBDRIVER_LOCAL_PATH, desired_capabilities=browser_capabilities)
    webdriver.set_window_size(1920, 1080)

    yield webdriver

    with allure.step('Driver teardown'):
        try:
            webdriver.quit()
        finally:
            webdriver.__class__._instances = {}
