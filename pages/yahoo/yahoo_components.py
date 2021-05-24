from core.locator import Locator


class YahooSearchBar:
    search_input = Locator('//*[@role="search"]//input[@type="text"]', 'Search Input')
    search_submit = Locator('//*[@role="search"]//input[@type="submit"]', 'Search Submit')
