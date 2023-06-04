import allure
from selenium.common.exceptions import InvalidSelectorException, StaleElementReferenceException

from core.driver import Driver
from core.exceptions import CustomBrokenException
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

    def _webelement_required(self):
        # magic function to update webelement if there is no webelement or if DOM element changed
        if not self.webelement:
            self.__call__()
            return
        try:
            # if not fails, webelement still has the DOM object link
            self.webelement.location
            return
        except StaleElementReferenceException:
            self.__call__()

    def __call__(self):
        try:
            self.webelement = Driver().find_element_by_xpath(self.xpath)
            return self
        except InvalidSelectorException:
            raise CustomBrokenException(f'Error: cannot locate {self.name}')

    def click(self, wait_for_new_page: bool = False):
        self._webelement_required()
        with allure.step(f'Click on {self.name}'):
            if wait_for_new_page:
                Driver().execute_script('var oldPage = 1;')
                self.webelement.click()
                wait_for_page_to_change()
                wait_for_page_to_load()
            else:
                self.webelement.click()

    def input(self, string: str):
        self._webelement_required()
        with allure.step(f'Input "{string}" into {self.name}'):
            self.webelement.send_keys(string)

    def is_on_page(self) -> bool:
        with allure.step(f'Check if element {self.name} is on page'):
            try:
                self.__call__()
                return True
            except:
                return False
