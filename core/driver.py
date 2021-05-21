from selenium.webdriver import Remote


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Driver(Remote, metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.implicitly_wait(5)  # default time waiting for a locator
