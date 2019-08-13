import re
from bs4 import BeautifulSoup

from locators.product_locators import ProductLocator
from parsers.product import ProductParser
from locators.page_locator import PagerLocator


class AllProductsPage:
    def __init__(self, page_content, website):
        self.soup = BeautifulSoup(page_content, 'html.parser')
        self.website = website

    @property
    def products(self):
        store_product_locator = ProductLocator.locator_selector(self, self.website)
        return [ProductParser(e) for e in self.soup.select(store_product_locator)]
        # for each product container in the parent object
    
    @property
    def page_count(self):
        return int(self.soup.select_one(PagerLocator.WILKO).attrs['data-total-pages'])