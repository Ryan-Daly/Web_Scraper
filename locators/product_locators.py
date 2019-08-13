class ProductLocator:
    store_locators = {
        'WILKO': "div.product-item.js-product-data",
    }

    def locator_selector(self, website):
        for key, val in ProductLocator.store_locators.items():
            if key.lower() == website:
                return val
    