import allure

from core.driver import Driver


class Page:
    """
    Main class for pages, contains locators
    """

    BASE_PAGE_URL = 'OverrideMe'

    def __init__(self):
        super().__init__()

    def open(self):
        with allure.step(f'Opening page "{self.__class__.__name__}"'):
            Driver().get(self.BASE_PAGE_URL)
            return self

    def open_with_path(self, path: str):
        with allure.step(f'Opening page "{self.__class__.__name__}" with additional path="{path}"'):
            Driver().get(self.BASE_PAGE_URL + path)
            return self

    @staticmethod
    def current_url() -> str:
        return Driver().current_url
