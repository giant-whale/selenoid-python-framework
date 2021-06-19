from core.locator import Locator
from core.page import Page
from pages.cloudmore.cloudmore_components import (
    CloudmoreFooter,
    CloudmoreHeader,
)


class __CloudmoreMarketingPageTemplate(Page):
    BASE_PAGE_URL = "https://web.cloudmore.com/"

    Header = CloudmoreHeader
    Footer = CloudmoreFooter


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
