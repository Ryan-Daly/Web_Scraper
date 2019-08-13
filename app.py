import requests, time, re

from pages.all_products_page import AllProductsPage

url = 'https://www.wilko.com/en-uk/pets/cats-kittens/cat-food-treats/c/1077'

page_content = requests.get(url).content


def website_parsed(url):
    pattern = '([a-z]+.co)'
    matcher = re.search(pattern, url)
    website = matcher.group(1)[:-3]
    return website

website = website_parsed(url)

page = AllProductsPage(page_content, website)

products = page.products

#for page_num in range(1, page.page_count):
#    page_content = requests.get(f'{url}?page={page_num}&pageSize=24').content
 #   page = AllProductsPage(page_content, website)
  #  products.extend(page.products)

print(products)