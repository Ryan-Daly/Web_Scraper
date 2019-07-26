import requests
import time

from pages.all_products_page import AllProductsPage


page_content = requests.get('https://www.wilko.com/en-uk/pets/cats-kittens/cat-food-treats/c/1077?page=0&pageSize=24').content


page = AllProductsPage(page_content)


print(page.products)