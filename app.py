import requests, time, re

from pages.all_products_page import AllProductsPage

url = 'https://www.wilko.com/en-uk/pets/cats-kittens/cat-food-treats/c/1077'

page_content = requests.get(url).content

page = AllProductsPage(page_content)

#def website_parsed(url):
    #pattern = '(www.[a-z]+.com)'
   # matcher = re.search(pattern, url)
  #  website = matcher.group(1)
 #   return f'{website}'

#website = website_parsed(url)

products = page.products

for page_num in range(1, page.page_count):
    page_content = requests.get(f'{url}?page={page_num}&pageSize=24').content
    page = AllProductsPage(page_content)
    products.extend(page.products)

print(products)