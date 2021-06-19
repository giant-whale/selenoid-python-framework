import random

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Chrome


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Driver(Chrome, metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.implicitly_wait(5)  # default time waiting for a locator

    def attach_screenshot(self):
        filename = f'screenshot session:{self.session_id}:{str(random.randint(0, 50000))}'
        allure.attach(self.get_screenshot_as_png(), name=filename, attachment_type=AttachmentType.PNG)
