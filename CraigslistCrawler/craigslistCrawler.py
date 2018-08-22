# !python 3

import requests
import bs4
import email.message
import smtplib
import sys
import CraigslistCrawler.craigstlistPost as cpost

baseUrl = "https://cnj.craigslist.org/search/"

def searchACategory(catCode):
    catUrl = baseUrl + catCode + '?'
    response = requests.get(catUrl, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    posts = soup.select('.result-row')
    return posts

def transformPost(post):
    title = ''
    date = ''
    location = ''
    price = ''
    url = ''
    subcategory = ''
    category = ''
    p = post.select_one('.result-info').getText
    date = post.select_one('.result-info').select_one('time').getText()
    title = post.select_one('.result-info').select_one('a').getText()
    url = post.select_one('.result-info').select_one('a["href"]').get('href')
    meta = post.select_one('.result-meta')

    if (meta.select_one('.result-hood') is not None):
        location = meta.select_one('.result-hood').get_text()
    if (meta.select_one('.result-price') is not None):
        price = meta.select_one('.result-price').get_text()

    p = cpost.CraigslistPost(url, title, date)
    p.location = location
    p.price = price
    p.category = category
    p.subcategory = subcategory

# start logic of loading craigslist page
# urlString = "https://cnj.craigslist.org/"
# response = requests.get(urlString, headers={'User-Agent': 'Mozilla/5.0'})
# response.raise_for_status()
# soup = bs4.BeautifulSoup(response.text, "html.parser")
#
# posts = soup.select('.rows')

somePosts = searchACategory('sof')
listOfPosts = []
listOfPosts.extend(list(map(lambda x: transformPost(x), somePosts)))


#start email logic
emailContent = """
    <html>
        <head>
            <meta http-equiv="Content=TYPE" content="text/html; charset=utf-8">
        </head>
        <body>
        <table>
            <thead>
                <tr>
                    <th></th>
                </tr>
            </thead>
            <tbody>
        
        </table>
            

"""

subject = "Craigslist Stuff"
msg = email.message.Message()
msg['SUBJECT'] = subject
msg['From'] = 'shicks255@yahoo.com'
msg['To'] = 'shicks255@yahoo.com'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(emailContent)

# try to send the email
try:
    smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
except smtplib.SMTPAuthenticationError as e:
    smtplib.quit()
    sys.exit()
    # log errors here

smtpObj.ehlo()
smtpObj.starttls()

try:
    smtpObj.login('shicks255@yahoo.com', '')
except smtplib.SMTPAuthenticationError as e:
    # more error logging
    smtpObj.quit()
    sys.exit()

message = msg.as_string().encode("utf-8")