import requests
import time
import re

from pages.all_products_page import AllProductsPage

url = 'https://www.wilko.com/en-uk/pets/cats-kittens/cat-food-treats/c/1077?page=0&pageSize=24'

#page_content = requests.get(url).content


#page = AllProductsPage(page_content)

#products = page.products

def website_parsed(url):
    pattern = '(https://www.[a-z]+.com/)'
    matcher = re.search(pattern, url)
    website = matcher.group(1)
    return f'{website}'

website = website_parsed(url)

#print(products)
print(website)