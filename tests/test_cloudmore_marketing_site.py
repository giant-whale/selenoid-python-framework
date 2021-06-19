import pytest

from core.driver import Driver
from pages.cloudmore.cloudmore_marketing_page import (
    CloudmoreMainPage,
    CloudmorePlatformPage,
    CloudmoreSolutionsPage,
    CloudmoreAboutUsPage,
    CloudmoreBlogPage,
    CloudmoreCaseStudiesPage,
    CloudmoreContactUsPage,
    CloudmoreSearchPage,
)


class TestCloudmoreDesktop:

    def test_cloudmore_mainpage_menu(self):
        page = CloudmoreMainPage().open()
        assert page.Header.logo().is_on_page()
        assert page.Header.platform_menu().is_on_page()
        assert page.Header.solutions_menu().is_on_page()
        assert page.Header.about_us_menu().is_on_page()
        assert page.Header.contact_us_menu().is_on_page()
        assert page.Header.blog_menu().is_on_page()
        assert page.Header.case_studies_menu().is_on_page()

    @pytest.mark.parametrize("page_to_open, locators", [
        (CloudmorePlatformPage, [CloudmorePlatformPage.Header.logo]),
        (CloudmoreSolutionsPage, [CloudmorePlatformPage.Header.logo]),
        (CloudmoreAboutUsPage, [CloudmoreAboutUsPage.Header.logo]),
        (CloudmoreBlogPage, [CloudmoreAboutUsPage.Header.logo]),
        (CloudmoreCaseStudiesPage, [CloudmoreAboutUsPage.Header.logo]),
        (CloudmoreContactUsPage, [CloudmoreContactUsPage.Header.logo, CloudmoreContactUsPage.Footer.contact_us_form,
                                  CloudmoreContactUsPage.contact_us_form])
    ])
    def test_cloudmore_page_contain_locators(self, page_to_open, locators):
        page_to_open().open()
        for locator in locators:
            assert locator().is_on_page()

    def test_cloudmore_search_and_screenshot_desktop(self):
        string_to_search = 'Högset'

        page = CloudmoreMainPage().open()
        page.Header.search_button().click()
        page.Search.search_input().input(string_to_search)
        page.Search.search_submit().click(wait_for_new_page=True)

        page = CloudmoreSearchPage()
        search_result = page.get_all_search_results()
        assert len(search_result) > 0

        page.navigate_to_page(3)
        Driver().attach_screenshot()


class TestCloudmoreMobile:

    @pytest.mark.mobile
    def test_cloudmore_search_and_screenshot_mobile(self):
        string_to_search = 'Högset'

        page = CloudmoreMainPage().open()
        page.Header.search_button().click()
        page.Search.search_input().input(string_to_search)
        page.Search.search_submit().click(wait_for_new_page=True)

        page = CloudmoreSearchPage()
        search_result = page.get_all_search_results()
        assert len(search_result) > 0

        page.navigate_to_page(3)
        Driver().attach_screenshot()
