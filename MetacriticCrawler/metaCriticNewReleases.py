# !python3
# coding=utf-8

import datetime
import email.message
import os
import smtplib
import sys

import bs4
import requests

from password import password


# Release Objects
class Release(object):
    artist = ""
    album = ""
    releaseDate = ""
    score = ""

    # Constructor
    def __init__(self, artist, album, releaseDate):
        self.artist = artist
        self.album = album
        self.releaseDate = releaseDate

    # to string
    def __str__(self):
        return str(self.__dict__)

# Function to make a release object from 4 parameters
def make_release(artist, album, releaseDate):
    release = Release(artist, album, releaseDate)
    return release

# Function to replace/rename log with tempLog
def close_log():
    for line in reversed(log_messages):
        LOG_FILE.write(line)
    for line in open("log.txt", "r").readlines():
        LOG_FILE.write(line)
    LOG_FILE.close()
    os.replace('tempLog.txt','log.txt')

# Function to add something to logList
def add_to_log(message):
    messageToAdd = datetime.datetime.now().strftime('\n%m-%d-%y %H:%M:%S:%f%p') + message;
    log_messages.append(messageToAdd)

# Start of logic here
os.chdir(sys.path[0])
# open log file
LOG_FILE = open("tempLog.txt", "a")
log_messages = []
add_to_log(" Info - Starting Metacritic Crawl....")

# get the reviews
url = 'http://www.metacritic.com/browse/albums/release-date/new-releases/date'
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

entries = soup.select('.product_wrap')

listOfNewReleases = []
newReleasesFile = open("newReleases.txt", "a+")

for entry in entries:
    album = ""
    artist = ""
    releaseDate = ""
    score = ""
    divs = entry.find_all('div')
    for div in divs:
        if 'product_title' in div.get('class'):
            album = div.getText()
            album = album.encode('ascii', errors='ignore').decode('ascii')
        if 'product_score' in div.get('class'):
            score = div.getText()
            score = score.encode('ascii', errors='ignore').decode('ascii')
        if div.find_all('li'):
            items = div.find_all('li')
            for item in items:
                if 'product_artist' in item.get('class'):
                    artist = item.find('span', {"class": "data"}).getText()
                    artist = artist.encode('ascii', errors='ignore').decode('ascii')
                if 'release_date' in item.get('class'):
                    releaseDate = item.find('span', {"class": "data"}).getText()
                    releaseDate = releaseDate.encode('ascii', errors='ignore').decode('ascii')

    fileRelease = make_release(artist, album, releaseDate)

    if str(fileRelease) not in open('newReleases.txt').read():
        listOfNewReleases.append(fileRelease)

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

add_to_log(" Info - Found " + str(len(listOfNewReleases)) + " new releases.")

for release in listOfNewReleases:
    emailContent += "<tr><td><b>" + release.artist + "</b><td>" + release.album + "</td><td>" + release.releaseDate + "</td><td>" + release.score + "</td></tr>"
    add_to_log(".........." + str(release))

emailContent += "</tbody></table></body></html>"

subject = "New releases as of " + datetime.datetime.now().strftime("%m-%d-%y %H:%M%p")
msg = email.message.Message()
msg['SUBJECT'] = subject
msg['From'] = 'shicks255@yahoo.com'
msg['To'] = 'shicks255@yahoo.com, sperovich4@gmail.com'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(emailContent)

# start the sending of emails
try:
    smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
except smtplib.SMTPException as e:
    add_to_log(" ERROR - " + str(e.args))
    smtpObj.quit()
    close_log()
    sys.exit()

smtpObj.ehlo()
smtpObj.starttls()

try:
    smtpObj.login('shicks255@yahoo.com', password)
except smtplib.SMTPAuthenticationError as e:
    add_to_log(" ERROR - " + str(e.args))
    smtpObj.quit()
    close_log()
    sys.exit()

message = msg.as_string().encode('utf-8')

if len(listOfNewReleases) > 0:
    try:
        # smtpObj.sendmail('shicks255@yahoo.com', 'shicks255@yahoo.com', message)
        smtpObj.sendmail('shicks255@yahoo.com', ['sperovich4@gmail.com', 'shicks255@yahoo.com'], message)
    except smtplib.SMTPSenderRefused as e:
        add_to_log(" ERROR - " + str(e.args))
        smtpObj.quit()
        close_log()
        sys.exit()

smtpObj.quit()

add_to_log(" Info - ..........Finished.")
close_log()

# if no errors, append the new releases file
for release in listOfNewReleases:
    newReleasesFile.write(str(release) + "\n")

sys.exit()