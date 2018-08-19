# !python 3

import requests
import bs4
import email.message
import smtplib
import sys
import CraigslistCrawler.CraigstlistPost

# start logic of loading craigslist page
urlString = "https://cnj.craigslist.org/"
response = requests.get(urlString, headers={'User-Agent': 'Mozilla/5.0'})
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, "html.parser")





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