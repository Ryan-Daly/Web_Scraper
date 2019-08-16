import re
from bs4 import BeautifulSoup

from locators.product_locators import ProductLocator
from parsers.product import ProductParser
from locators.page_locator import PagerLocator


class AllProductsPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def products(self):
        return [ProductParser(e) for e in self.soup.select(ProductLocator.locator_selector)]
        # for each product container in the parent object
    
    @property
    def page_count(self):
        return int(self.soup.select_one(PagerLocator.locator_selector).attrs['data-total-pages'])