import requests, time, re, config

from pages.all_products_page import AllProductsPage

page_content = requests.get(config.url).content

page = AllProductsPage(page_content)

products = page.products

#for page_num in range(1, page.page_count):
#    page_content = requests.get(f'{url}?page={page_num}&pageSize=24').content
 #   page = AllProductsPage(page_content, website)
  #  products.extend(page.products)

print(products)