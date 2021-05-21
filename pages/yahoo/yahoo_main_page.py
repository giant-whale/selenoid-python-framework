from core.page import Page
from pages.yahoo.yahoo_components import YahooSearchBar


class YahooMainPage(Page):
    BASE_PAGE_URL = "https://www.yahoo.com/"

    YahooSearchBar = YahooSearchBar()
