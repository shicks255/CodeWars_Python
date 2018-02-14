# !python3

import requests
import bs4


class Release(object):
    artist = ""
    album = ""
    releaseDate = ""
    score = ""

    # Constructor
    def __init__(self, artist, album, releaseDate, score):
        self.artist = artist
        self.album = album
        self.releaseDate = releaseDate
        self.score = score

    # to string
    def __str__(self):
        return str(self.__dict__)


def make_release(artist, album, releaseDate, score):
    release = Release(artist.strip(), album.strip(), releaseDate.strip(), score.strip())
    return release


url = 'http://www.metacritic.com/browse/albums/release-date/new-releases/date'
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

entries = soup.select('.product_wrap')

listOfNewReleases = []
file = open("newReleases.txt", "a+")

for entry in entries:
    album = ""
    artist = ""
    releaseDate = ""
    score = ""
    divs = entry.find_all('div')
    for div in divs:
        if 'product_title' in div.get('class'):
            album = div.getText()
        if 'product_score' in div.get('class'):
            score = div.getText()
        if div.find_all('li'):
            items = div.find_all('li')
            for item in items:
                if 'product_artist' in item.get('class'):
                    artist = item.find('span', {"class": "data"}).getText()
                if 'release_date' in item.get('class'):
                    releaseDate = item.find('span', {"class": "data"}).getText()

    release = make_release(artist, album, releaseDate, score)

    if str(release) not in open('newReleases.txt').read():
        file.write(str(release)+"\n")
        listOfNewReleases.append(release)



print(len(listOfNewReleases))

