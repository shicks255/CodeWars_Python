# !python3
# coding=utf-8

import requests
import bs4
import smtplib
import datetime
import email.message
import os
import sys

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

# Function to replace/rename log with tempLog
def close_log():
    for line in open("log.txt", "r").readlines():
        LOG_FILE.write(line)
    LOG_FILE.close()
    os.replace('tempLog.txt', 'log.txt')

# Start of logic here

# open log file
LOG_FILE = open("tempLog.txt", "a")

# get the reviews
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


subject = "New releases as of " + datetime.datetime.now().strftime("%m-%d-%y %H:%M%p")

emailContent = """
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body>
        <table>
            <thead>
                <tr>
                    <th>Artist</th>
                    <th>Album</th>
                    <th>Release Date</th>
                    <th>Score</th>
                </tr>
            </thead>
            <tbody>
"""

LOG_FILE.write(datetime.datetime.now().strftime("\n%m-%d-%y %H:%M:%S:%f%p") + " Info - Starting Metacritic Crawl.....")
LOG_FILE.write(datetime.datetime.now().strftime("\n%m-%d-%y %H:%M:%S:%f%p") + " Info - Found " + str(len(listOfNewReleases)) + " new releases.")

for release in listOfNewReleases:
    emailContent += "<tr><td><b>" + release.artist + "</b><td>" + release.album + "</td><td>" + release.releaseDate + "</td><td>" + release.score + "</td></tr>"
    LOG_FILE.writable(".........." + str(release)+"\n")

emailContent += "</tbody></table>"
emailContent += "</body></html>"

msg = email.message.Message()
msg['SUBJECT'] = subject
msg['From'] = 'shicks255@yahoo.com'
msg['To'] = 'shicks255@yahoo.com'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(emailContent)

# start the sending of emails
try:
    smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
except smtplib.SMTPException as e:
    LOG_FILE.write(datetime.datetime.now().strftime("\n%m-%d-%y %H:%M:%S:%f%p") + " ERROR - " + str(e.args))
    smtpObj.quit()
    close_log()
    sys.exit()

smtpObj.ehlo()
smtpObj.starttls()

try:
    smtpObj.login('shicks255@yahoo.com', '')
except smtplib.SMTPAuthenticationError as e:
    LOG_FILE.write(datetime.datetime.now().strftime("\n%m-%d-%y %H:%M:%S:%f%p") + " ERROR - " + str(e.args))
    smtpObj.quit()
    close_log()
    sys.exit()

message = msg.as_string().encode('utf-8')

try:
    smtpObj.sendmail('shicks255@yahoo.com', 'shicks255@yahoo.com', message)
except smtplib.SMTPSenderRefused as e:
    LOG_FILE.write(datetime.datetime.now().strftime("\n%m-%d-%y %H:%M:%S:%f%p") + " ERROR - " + str(e.args))
    smtpObj.quit()
    close_log()
    sys.exit()

smtpObj.quit()

LOG_FILE.write(datetime.datetime.now().strftime("\n%m-%d-%y %H:%M:%S:%f%p") + " Info - ..........Finished")
close_log()