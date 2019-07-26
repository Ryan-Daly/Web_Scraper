import re

from locators.product_element_locators import ProductElementLocators


class ProductParser:
    def __init__(self, parent):
        self.parent = parent    # product container = parent

    def __repr__(self):
        return f'Product {self.price}'

    @property
    def name(self):
        locator = ProductElementLocators.NAME
        product_name = self.parent.select_one(locator).attrs['title']
        print(product_name)
        return product_name

    @property
    def link(self):
        locator = ProductElementLocators.LINK
        product_link = self.parent.select_one(locator).attrs['href']
        return f'https://www.ocado.com{product_link}'

    @property
    def price(self):
        locator = ProductElementLocators.PRICE
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        product_price = float(matcher.group(1))
        return product_price

    @property
    def quantity(self):
        locator = ProductElementLocators.QUANTITY
        product_quantity = self.parent.select_one(locator).string
        return product_quantity

    @property
    def offer(self):
        locator = ProductElementLocators.OFFER
        product_offer = self.parent.select_one(locator).string
        return product_offer