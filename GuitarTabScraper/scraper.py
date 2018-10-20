# !python3
import re

import bs4
import requests
import json

class tab(object):
    content = ""
    rating = ""
    votes = ""
    name = ""
    artist = ""
    album = ""
    type = ""
    date = ""

# https://www.ultimate-guitar.com/explore?type[]=Chords
# https://www.ultimate-guitar.com/explore?type[]=Tabs

# this is the URl that will print a list of search results
urlChords = 'https://www.ultimate-guitar.com/explore?type[]=Chords'
urlTabs = 'https://www.ultimate-guitar.com/explore?type[]=Tabs'
urlSlayer = 'https://www.ultimate-guitar.com/artist/slayer_459'

urlSlayerTabs = urlSlayer + '?filter=tabs'

res = requests.get(urlSlayerTabs, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
results = soup.prettify()

regex1 = re.compile('(\"other_tabs\":)(.*?)}]')
mo = regex1.search(results)
if mo:
    textChunk = str(mo.groups())
    textChunk = textChunk.replace('(\'\"other_tabs\":\', \'[{', '')
    tabs = str(textChunk).split('},{')
    for tab in tabs:
        print('\r\n')
        print(tab)
        if tab[-1:] == ')':
            tab = tab.rstrip(')')
            tab = tab.rstrip('\'')
        tab = ''.join(('[{', tab, '}]'))
        tabData = json.loads(tab)


# start = results.find('{\"artist_name\":')
# end = results.find('header_bidding')
# results = results[start:end]

# to get the tabs
# regex = re.compile('(\{\"id\":)(.*?)((\]\}\}))')
# to get the artist url when searching for artist
# regex = re.compile('artist/(.*?)\"')
# mo = regex.search(results)
#
# if mo:
#     print(mo.groups())


# to get the actual tab chunk
# url = 'https://tabs.ultimate-guitar.com/tab/slayer/read_between_the_lies_tabs_82754'
# res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# results = soup.prettify()
#
# regex = re.compile('\"content\":(.*?)\}')
# mo = regex.search(results)
# if mo:
#     print(mo.groups())





