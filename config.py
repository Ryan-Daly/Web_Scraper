url = 'https://www.wilko.com/en-uk/pets/cats-kittens/cat-food-treats/c/1077'

def website_parsed(url):
    pattern = '([a-z]+.co)'
    matcher = re.search(pattern, url)
    website = matcher.group(1)[:-3]
    return website

website = website_parsed(url)