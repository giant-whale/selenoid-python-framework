import allure

from core.driver import Driver
from core.helpers import (
    wait_for_page_to_change,
    wait_for_page_to_load,
)


class Locator:
    """
    Present locators on pages
    """
    xpath = None
    webelement = None
    name = None

    def __init__(self, name: str, xpath: str):
        self.xpath = xpath
        self.name = name

    def __call__(self):
        self.webelement = Driver().find_element_by_xpath(self.xpath)
        return self

    def click(self, wait_for_new_page: bool = False):
        with allure.step(f'Click on {self.name}'):
            if wait_for_new_page:
                Driver().execute_script('var oldPage = 1;')
                self.webelement.click()
                wait_for_page_to_change()
                wait_for_page_to_load()
            else:
                self.webelement.click()

    def input(self, string: str):
        with allure.step(f'Input "{string}" into {self.name}'):
            self.webelement.send_keys(string)

    def is_on_page(self) -> bool:
        with allure.step(f'Check if element {self.name} is on page'):
            return self.webelement.is_displayed()
