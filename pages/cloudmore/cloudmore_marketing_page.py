import allure

from core.driver import Driver
from core.locator import Locator
from core.page import Page
from pages.cloudmore.cloudmore_components import (
    CloudmoreFooter,
    CloudmoreHeader,
    CloudmoreSearch,
)


def hide_cookies_message():
    cookies_message_cookie = '__hs_initial_opt_in'
    if not Driver().get_cookie(cookies_message_cookie):
        Driver().add_cookie({'name': cookies_message_cookie, 'value': 'true'})
        Driver().refresh()


class __CloudmoreMarketingPageTemplate(Page):
    BASE_PAGE_URL = "https://web.cloudmore.com/"

    Header = CloudmoreHeader
    Footer = CloudmoreFooter
    Search = CloudmoreSearch

    cookies_block = Locator('Cookies block', '//div[@id="hs-eu-cookie-confirmation"]')

    def open(self):
        super().open()
        hide_cookies_message()
        return self

    def open_with_path(self, path: str):
        super().open_with_path(path=path)
        hide_cookies_message()
        return self


class CloudmoreMainPage(__CloudmoreMarketingPageTemplate):
    ...


class CloudmorePlatformPage(__CloudmoreMarketingPageTemplate):
    BASE_PAGE_URL = "https://web.cloudmore.com/product"


class CloudmoreSolutionsPage(__CloudmoreMarketingPageTemplate):
    BASE_PAGE_URL = "https://web.cloudmore.com/solutions"


class CloudmoreAboutUsPage(__CloudmoreMarketingPageTemplate):
    BASE_PAGE_URL = "https://web.cloudmore.com/about-us"


class CloudmoreContactUsPage(__CloudmoreMarketingPageTemplate):
    BASE_PAGE_URL = "https://web.cloudmore.com/contact-us"

    xpath_base = '//div[@class="body-container-wrapper"]/div/div[contains(@class, "row-number-1")]'
    contact_us_form = Locator('Contact Us form on page', xpath_base+'//form')


class CloudmoreBlogPage(__CloudmoreMarketingPageTemplate):
    BASE_PAGE_URL = "https://web.cloudmore.com/blog"


class CloudmoreCaseStudiesPage(__CloudmoreMarketingPageTemplate):
    BASE_PAGE_URL = "https://web.cloudmore.com/case-studies"


class CloudmoreSearchPage(__CloudmoreMarketingPageTemplate):
    BASE_PAGE_URL = "https://web.cloudmore.com/hs-search-results"

    search_result_record = Locator('Search result row', '//div[@class="hs-search-results"]/ul/li')
    next_page_button = Locator('Next page button', '//div[@class="hs-search-results"]//*[contains(@class,"next-page")]')
    previous_page_button = Locator('Previous page button', '//div[@class="hs-search-results"]//*[contains(@class,"prev-page")]')

    def get_all_search_results(self):
        self.search_result_record().wait_for_element()
        return self.search_result_record.get_all_entities()

    def navigate_to_page(self, page: int, pass_if_no_next_page: bool = True):
        with allure.step(f'Navigating to {page} page, '
                         f'opened page can be the last and lower index: {pass_if_no_next_page}'):
            if pass_if_no_next_page:
                try:
                    for _ in range(0, page):
                        self.next_page_button().click(wait_for_new_page=True)
                except:
                    pass
            else:
                for _ in range(0, page):
                    self.next_page_button().click(wait_for_new_page=True)
