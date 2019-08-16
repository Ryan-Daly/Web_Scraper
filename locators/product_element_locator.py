import config

class ProductElementLocators:
    store_element_locators = {
        'WILKO': {
            'NAME': "data-product-name",
            'LINK': 'div.details a.product-link.name',
            'PRICE': '',
            'QUANTITY': '',
            'OFFER': '',
        },
    }
    
    def locator_selector(self, element):
        for key, val in ProductElementLocators.store_element_locators.items():
            if key.lower() == config.website:
                print(val[element])