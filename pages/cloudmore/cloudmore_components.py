from core.locator import Locator


class CloudmoreHeader:
    xpath_base = '//div[@class="header-container-wrapper"]/div/div[contains(@class, "row-number-1")]'
    block = Locator('Header block', xpath_base)

    logo = Locator('Header logo 1x', xpath_base+'//*[@data-widget-type="logo"]')
    platform_menu = Locator('Solutions button', xpath_base+'//ul//a[.="Platform"]')
    solutions_menu = Locator('Solutions button', xpath_base+'//ul//a[.="Solutions"]')
    about_us_menu = Locator('Solutions button', xpath_base+'//ul//a[.="About Us"]')
    contact_us_menu = Locator('Solutions button', xpath_base+'//ul//a[.="Contact us"]')
    blog_menu = Locator('Solutions button', xpath_base+'//ul//a[.="Blog"]')
    case_studies_menu = Locator('Solutions button', xpath_base+'//ul//a[.="Case Studies"]')


class CloudmoreFooter:
    xpath_base = '//div[@class="footer-container-wrapper"]/div/div[contains(@class, "row-number-1")]'
    block = Locator('Footer block', xpath_base)

    contact_us_form = Locator('Contact Us form on footer', xpath_base+'//form')
