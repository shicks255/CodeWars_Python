 # !python 3


class CraigslistPost(object):
    url = ''
    title = ''
    postDate = ''
    location = ''

    # Constructor
    def __init__(self, url, title, postDate, location):
        self.url = url
        self.title = title
        self.postDate = postDate
        self.location = location

    # ToString
    def __str__(self):
        return self.title + ' ' + self.postDate + ' ' + self.location

