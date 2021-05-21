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

    def __init__(self, xpath: str):
        self.xpath = xpath

    def __call__(self):
        self.webelement = Driver().find_element_by_xpath(self.xpath)
        return self

    def click(self, wait_for_new_page: bool = False):
        if wait_for_new_page:
            Driver().execute_script('var oldPage = 1;')
            self.webelement.click()
            wait_for_page_to_change()
            wait_for_page_to_load()
        else:
            self.webelement.click()

    def input(self, string: str):
        self.webelement.send_keys(string)

    def is_on_page(self) -> bool:
        return self.webelement.is_displayed()
