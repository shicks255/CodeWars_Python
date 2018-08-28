# !python 3

import requests
import bs4
import email.message
import smtplib
import sys
import CraigslistCrawler.craigstlistPost as cpost
import CraigslistCrawler.Categories as cats

baseUrl = "https://cnj.craigslist.org/search/"

def searchACategory(catCode):
    catUrl = baseUrl + catCode + '?'
    response = requests.get(catUrl, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    posts = soup.select('.result-row')
    return posts

def transformPost(post, category, subcategory):
    title = ''
    date = ''
    location = ''
    price = ''
    url = ''
    if (post.select_one('.result-info') is not None):
        resultInfo = post.select_one('.result-info')
        if (resultInfo.select_one('time') is not None):
            date = resultInfo.select_one('time').getText()
        if (resultInfo.select_one('a') is not None):
            title = resultInfo.select_one('a').getText()
        if (resultInfo.select_one('a["href"]') is not None):
            url = resultInfo.select_one('a["href"]').get('href')

    meta = post.select_one('.result-meta')
    if (meta.select_one('.result-hood') is not None):
        location = meta.select_one('.result-hood').get_text()
    if (meta.select_one('.result-price') is not None):
        price = meta.select_one('.result-price').get_text()

    return cpost.CraigslistPost(url, title, date, location, category, subcategory, price)

listOfPostObjects = []
categories = cats.categories

for cat in categories:
    posts = searchACategory(cat[2])
    listOfPostObjects.extend(list(map(lambda x: transformPost(x, cat[0], cat[1]), posts)))


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
                    <th>Title</th>
                    <th>Date</th>
                    <th>Location</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
"""


category = ''
subcategory = ''
for post in listOfPostObjects:
    if category != post.category or subcategory != post.subcategory:
        category = post.category
        subcategory = post.subcategory
        emailContent += """
        <tr>
            <td colspan="4"><b>""" + category + "-" + subcategory +"""</b></td>
        </tr>
        """

    emailContent += """
        <tr>
            <td>""" + post.title + """"</td>
            <td>""" + post.postDate + """"</td>
            <td>""" + post.location + """"</td>
            <td>""" + post.price + """"</td>
        </tr>
    """

emailContent += """
            </tbody>
        </table>
        </body>
    </html>
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