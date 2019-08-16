import config

class PagerLocator:
    store_pagers = {
        'WILKO': 'div.load-more-products',
    }

    @property
    def locator_selector(self):
        for key, val in PagerLocator.store_pagers.items():
            if key.lower() == config.website:
                return val
    