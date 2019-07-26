import re

from locators.product_locators import ProductLocator
from parsers.product import ProductParser
from bs4 import BeautifulSoup


class AllProductsPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def products(self):
        return [ProductParser(e) for e in self.soup.select(ProductLocator.WILKO)]
        # for each product container in the parent object