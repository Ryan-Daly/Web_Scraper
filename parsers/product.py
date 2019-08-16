import re

from locators.product_element_locator import ProductElementLocators


class ProductParser:
    def __init__(self, parent):
        self.parent = parent    # product container = parent

    def __repr__(self):
        return f'\nProduct: {self.name} *** {self.price} *** {self.link}'

    @property
    def name(self):
        locator = ProductElementLocators.locator_selector(self, 'NAME')
        product_name = self.parent[locator]
        product_name = re.sub(' +', ' ', product_name)
        return product_name

    @property
    def link(self):
        locator = ProductElementLocators.locator_selector(self, 'LINK')
        product_link = self.parent.select_one(locator).attrs['href']
        return product_link

    @property
    def price(self):
        #locator = ProductElementLocators.locator_selector('PRICE')
        item_price = self.parent.attrs['data-price']

        pattern = '([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        product_price = format(float(matcher.group(1)), '.2f')
        return f'£{product_price}'
        
    @property
    def quantity(self):
        locator = ProductElementLocators.locator_selector(self, 'QUANTITY')
        product_quantity = self.parent.select_one(locator).string
        return product_quantity

    @property
    def offer(self):
        locator = ProductElementLocators.locator_selector(self, 'OFFER')
        product_offer = self.parent.select_one(locator).string
        return product_offer