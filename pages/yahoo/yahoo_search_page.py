from core.locator import Locator
from core.page import Page
from pages.yahoo.yahoo_components import YahooSearchBar


class YahooSearchPage(Page):
    BASE_PAGE_URL = "https://search.yahoo.com/search?p="

    YahooSearchBar = YahooSearchBar()
    result_number = Locator('Result Number', '//*[contains(@class,"searchSuperTop")]//span')

    class Header:
        home_logo = Locator('Home Logo', '//a[@id="logo"]')
