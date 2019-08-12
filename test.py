products = [
    {
        'name': 'hair dryer',
        'price': 13.99,
        'link': 'me1',
    },
    {
        'name': 'monster',
        'price': 1.04,
        'link': 'me2'
    }
]


# print(results['products'][1]['price'])        # prints 1.04

#for product in products:
 #   if product['name'] == 'shampoo':
  #      product['quantity'] = 5

amazon = [
    {
        'title': 'ribena',
        'price': 3.02,
        'asin': 'B009123'
    },
    {
        'title': 'monster',
        'price': 5.99,
        'asin': 'B05263'
    },
    {
        'title': 'quilt',
        'price': 7.63,
        'asin': 'B009883'
    },
]

def price_diff(prod_price, amz_price):
    return amz_price - prod_price

for product in products:
    for i in amazon:
        if product['name'] == i['title']:
            product['asin'] = i['asin']
            product['amz_price'] = i['price']
            product['difference'] = price_diff(product['price'], product['amz_price'])
            print(product)

