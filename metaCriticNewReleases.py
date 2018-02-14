# !python3

import requests
import bs4
import os

url = 'http://www.metacritic.com/browse/albums/release-date/new-releases/date'
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

entries = soup.select('.product_wrap')

releases = [entries.__sizeof__()]

# file = os.open("newReleases.txt", 0)

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

    print(artist.strip() + " " + album.strip() + " " + score.strip() + " " + releaseDate.strip())

