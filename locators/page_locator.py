class PagerLocator:
    store_pagers = {
        'WILKO' = 'div.load-more-products'
    }

    def locator_selector(self, website):
        for key, val in PagerLocator.store_pagers.items():
            if key.lower() == website:
                return val
    