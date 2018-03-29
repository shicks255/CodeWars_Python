# !python3
# coding=utf-8

import requests
import bs4
import smtplib
import datetime
import email.message
import os
import sys
import unicodedata

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
    release = Release(artist, album, releaseDate, score)
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
            album = unicodedata.normalize('NFKD', album)
        if 'product_score' in div.get('class'):
            score = div.getText()
            # score = unicodedata.normalize('NFKD', score).encode('ASCII', 'ignore')
        if div.find_all('li'):
            items = div.find_all('li')
            for item in items:
                if 'product_artist' in item.get('class'):
                    artist = item.find('span', {"class": "data"}).getText()
                    artist = unicodedata.normalize('NFKD', artist)
                if 'release_date' in item.get('class'):
                    releaseDate = item.find('span', {"class": "data"}).getText()
                    releaseDate = unicodedata.normalize('NFKD', releaseDate)

    release = make_release(artist, album, releaseDate, score)

    if str(release) not in open('newReleases.txt').read():
        file.write(str(release)+"\n")
        listOfNewReleases.append(release)

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
msg['To'] = 'shicks255@yahoo.com'
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
    smtpObj.login('shicks255@yahoo.com', '')
except smtplib.SMTPAuthenticationError as e:
    add_to_log(" ERROR - " + str(e.args))
    smtpObj.quit()
    close_log()
    sys.exit()

message = msg.as_string().encode('utf-8')

if len(listOfNewReleases) > 0:
    try:
        smtpObj.sendmail('shicks255@yahoo.com', 'shicks255@yahoo.com', message)
    except smtplib.SMTPSenderRefused as e:
        add_to_log(" ERROR - " + str(e.args))
        smtpObj.quit()
        close_log()
        sys.exit()

smtpObj.quit()

add_to_log(" Info - ..........Finished.")
close_log()