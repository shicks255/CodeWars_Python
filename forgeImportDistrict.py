# !python3

import bs4
import requests
import sys
import os

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

goSheetUrl = open("C:\\Users\\steveh.AZEROTH\\Desktop\\goz.html")

# res = bs4.BeautifulSoup(goSheetUrl.read())
soup = bs4.BeautifulSoup(goSheetUrl.read())

notecards = soup.select('div')

for card in notecards:
    if 'notecard' in card.get('class'):
        if 'SchoolFi' in card.find('b').getText():
            districts = card.find_all('tr')
            for district in districts:
                if district.get('data-type'):
                    if 'customer' in district.get('data-type'):
                        print(district.find('a').get('href'))
