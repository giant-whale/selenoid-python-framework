from core.locator import Locator, Input


class YahooSearchBar:
    search_input = Input('Search Input', '//*[@role="search"]//input[@type="text"]')
    search_submit = Locator('Search Submit', '//button[@id="ybar-search"]')
