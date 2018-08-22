 # !python 3


class CraigslistPost(object):
    url = ''
    title = ''
    postDate = ''
    location = ''
    category = ''
    subcategory = ''
    price = ''

    # Constructor
    def __init__(self, url, title, postDate, location, category, subcategory, price):
        self.url = url
        self.title = title
        self.postDate = postDate
        self.location = location
        self.category = category
        self.subcategory = subcategory
        self.price = price

    # ToString
    def __str__(self):
        return self.title + ' ' + self.postDate + ' ' + self.location

