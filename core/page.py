from core.driver import Driver


class Page:
    """
    Main class for pages, contains locators
    """

    BASE_PAGE_URL = 'OverrideMe'

    def __init__(self):
        super().__init__()

    def open(self):
        Driver().get(self.BASE_PAGE_URL)
        return self

    def open_with_path(self, path: str):
        Driver().get(self.BASE_PAGE_URL + path)
        return self

    @staticmethod
    def current_url() -> str:
        return Driver().current_url
