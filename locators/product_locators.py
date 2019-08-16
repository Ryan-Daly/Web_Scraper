import config

class ProductLocator:
    store_locators = {
        'WILKO': 'div.product-item.js-product-data',
    }


    @property
    def locator_selector(self):
        for key, val in ProductLocator.store_locators.items():
            if key.lower() == config.website:
                return val
    