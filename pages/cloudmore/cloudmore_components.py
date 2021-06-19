from core.locator import Locator


class CloudmoreHeader:
    xpath_base = '//div[@class="header-container-wrapper"]/div/div[contains(@class, "row-number-1")]'
    block = Locator('Header block', xpath_base)

    logo = Locator('Header logo', xpath_base+'//*[@data-widget-type="logo"]')
    platform_menu = Locator('Platform button', xpath_base+'//ul//a[.="Platform"]')
    solutions_menu = Locator('Solutions button', xpath_base+'//ul//a[.="Solutions"]')
    about_us_menu = Locator('About Us button', xpath_base+'//ul//a[.="About Us"]')
    contact_us_menu = Locator('Contact Us button', xpath_base+'//ul//a[.="Contact us"]')
    blog_menu = Locator('Blog button', xpath_base+'//ul//a[.="Blog"]')
    case_studies_menu = Locator('Case Studies button', xpath_base+'//ul//a[.="Case Studies"]')
    search_button = Locator('Search button', xpath_base+'//span[contains(@class, "search")]')


class CloudmoreFooter:
    xpath_base = '//div[@class="footer-container-wrapper"]/div/div[contains(@class, "row-number-1")]'
    block = Locator('Footer block', xpath_base)

    contact_us_form = Locator('Contact Us form on footer', xpath_base+'//form')


class CloudmoreSearch:
    xpath_base = '//div[contains(@class, "fullscreen-search")]'

    search_form = Locator('Search form', xpath_base+'//form')
    search_input = Locator('Search input', xpath_base+'//form/input')
    search_submit = Locator('Search submit', xpath_base+'//form/button')
