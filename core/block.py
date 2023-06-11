from __future__ import annotations

from core.driver import Driver
from core.locator import Locator


class Block:
    """
    What is it for:
        Structure for non-unic containers of items, allows to interact with all of them

    Definition:
        container = Block('Example block', '//div',
                          title = Locator('Title', '//h1'),
                          body = Locator('Body', '//div'),
                          field = Input('Value Input', '//input'),
                    )

    Usage, when only first element needed:
        container.field.input('test value')
        container.title.click()

    Usage, when all elements needed:
        for _container in container.get_all_blocks():
            _container.field.input('test value')

    """

    def __init__(self, name: str, xpath: str, **kwargs: {str, Locator}):
        self._name = name
        self._xpath = xpath
        for _locator_class_name, _locator_object in kwargs.items():
            self.__dict__[_locator_class_name] = _locator_object
        self._update_locators()

    def _update_locators(self):
        for value in self.__dict__.values():
            if isinstance(value, Locator):
                value.block_xpath = self._xpath
                value.name = f'{self._name} > {value.name}'

    def get_all_blocks(self) -> [Block]:
        all_blocks = []
        for element in Driver().find_elements_by_xpath(self._xpath):
            block = self.__class__(self._name, self._xpath, _webelement=element)
            # put Locators in new Block
            for name, value in self.__dict__.items():
                if isinstance(value, Locator):
                    _locator = value.__class__(f'{block._name} > {value.name}', value.xpath)
                    _locator.parent = element
                    block.__dict__[name] = _locator
            all_blocks.append(block)
        return all_blocks
