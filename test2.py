url = 'wilko'

class Ryan:
    finders = {
        'WILKO': "div.product-item.js-product-data",
        'ASDA': 'Blue Bananas'
    }

    @property
    def product_locator_selector(website):
        for key, val in finders.items():
            if key.lower() == website:
                print(val)
    