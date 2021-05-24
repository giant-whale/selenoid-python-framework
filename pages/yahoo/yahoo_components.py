from core.locator import Locator


class YahooSearchBar:
    search_input = Locator('Search Input', '//*[@role="search"]//input[@type="text"]')
    search_submit = Locator('Search Submit', '//*[@role="search"]//input[@type="submit"]')
