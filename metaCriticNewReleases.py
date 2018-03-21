# !python3
# coding=utf-8

import requests
import bs4
import smtplib
import datetime

# Release Objects
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

# Function to make a release object from 4 parameters
def make_release(artist, album, releaseDate, score):
    release = Release(artist.strip(), album.strip(), releaseDate.strip(), score.strip())
    return release

# Start of logic here
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

    for release in listOfNewReleases:
        pass



print(len(listOfNewReleases))

# start the sending of emails
smtpObj = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
smtpObj.ehlo()
# smtpObj.starttls()
smtpObj.login('shicks255@yahoo.com', '')

subject = "New releases as of " + datetime.datetime.now().strftime("%d-%m-%y %H:%M%p")
body = "Artist - Album - Release Date - Score"
for release in listOfNewReleases:
    body += "\n<b>" + release.artist + "</b> " + release.album + " " + release.releaseDate + " <b>" + release.score + "</b>"

print(subject)
print(body)

smtpObj.sendmail("shicks255@yahoo.com", "shicks255@yahoo.com", body.encode('utf-8'))
smtpObj.quit()

