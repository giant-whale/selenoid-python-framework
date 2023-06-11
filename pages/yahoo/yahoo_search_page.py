from core.block import Block
from core.locator import Locator
from core.page import Page
from pages.yahoo.yahoo_components import YahooSearchBar


class YahooSearchPage(Page):
    BASE_PAGE_URL = "https://search.yahoo.com/search?p="

    YahooSearchBar = YahooSearchBar()
    result_number = Locator('Result Number', '//*[contains(@class,"searchSuperTop")]//span')
    result_item = Block('Result Item', '//ol[contains(@class, "searchCenterMiddle")]/li/div[contains(@class, "relsrch")]',
                        title=Locator('Title', '//h3[contains(@class, "title")]'),
                        preview=Locator('Preview text', '//div[contains(@class, "compText")]'))

    class Header:
        home_logo = Locator('Home Logo', '//a[@id="logo"]')
