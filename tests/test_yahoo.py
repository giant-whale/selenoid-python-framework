import pytest

from pages.yahoo.yahoo_main_page import YahooMainPage
from pages.yahoo.yahoo_main_page_mobile import YahooMainPageMobile
from pages.yahoo.yahoo_search_page import YahooSearchPage


class TestYahoo:

    def test_yahoo_mainpage_search(self):
        page = YahooMainPage().open()
        page.YahooSearchBar.search_input.input('Yahoo Search')
        page.YahooSearchBar.search_submit.click(wait_for_new_page=True)
        assert YahooSearchPage().result_number.is_on_page()

    def test_yahoo_search_navigate_to_mainpage(self):
        page = YahooSearchPage().open_with_path('Yahoo Search')
        page.Header.home_logo.click(wait_for_new_page=True)
        assert page.current_url() == YahooMainPage.BASE_PAGE_URL

    @pytest.mark.mobile
    def test_yahoo_mainpage_mobile(self):
        page = YahooMainPageMobile().open()
        page.menu_button.click()
        assert page.is_menu_displayed()
