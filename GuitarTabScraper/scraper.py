# !python3
import re
import sys

import bs4
import requests
import json

class Tab(object):
    content = ''
    songTitle = ''
    artistName = ''
    type = ''
    version = ''
    votes = ''
    rating = ''
    date = ''
    tabUrl = ''
    tuning = ''
    typeName = ''
    ugId = ''

MAIN_URL = 'https://www.ultimate-guitar.com/'

# search the entered Artist arg for a URl to start scraping on.
def getArtistURL(artistName):
    artistSearchName = artistName.replace(' ', '%20')
    res = requests.get(MAIN_URL + 'search.php?search_type=band&value=' + artistSearchName)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    results = soup.prettify()

    # regex = re.compile('\"artist_name\":(.*?)\"tabs_cnt\"')
    regex = re.compile('(\"results\":.*?}}]})')
    mo = regex.search(results)
    if mo:
        artistResults = str(mo.groups())
        regex2 = re.compile('{(.*?)]}}')
        mo2 = regex2.findall(artistResults)
        for x in mo2:
            print(x)
            thisArtistNameIndex = x.find('\"artist_name\":')
            thisArtistName = x[thisArtistNameIndex+15 : x.find('\"artist_url\"')-2]
            if thisArtistName.lower() == artistName.lower():
                thisArtistUrlIndex = x.find('\"artist_url\"')
                thisArtistUrl = x[thisArtistUrlIndex+14 : x.find('\"tabs_cnt\"')-2]
                return thisArtistUrl.replace('\\', '')
                print(thisArtistUrl)


# this is where the heavy lifting is done, remember to add CHORDS
def scrapTabs(artistUrl):
    payloadTabs = []

    keepGoing = True
    pageNumber = 1
    while keepGoing:
        # scrapUrl = artistUrl + '?pageNumber=' + str(pageNumber) + '&filter=tabs'
        params = {'page': str(pageNumber)}
        pageNumber += 1

        res = requests.get(artistUrl, headers={'User-Agent': 'Mozilla/5.0'}, params=params)
        print(str(res.status_code) + ' for page number ' + str(pageNumber-1))
        if res is None or res.status_code != 200:
            keepGoing = False
            continue

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
                if tab[-1:] == ')':
                    tab = tab.rstrip(')')
                    tab = tab.rstrip('\'')
                tab = ''.join(('{', tab, '}'))
                tab = tab.replace('\\\\"', '')
                tab = tab.replace('\\\'', '')
                try:
                    tabData = json.loads(tab)
                except json.decoder.JSONDecodeError:
                    print('error with ' + tab)
                    continue

                if 'marketing_type' in tabData.keys():
                    continue

                songTitle = tabData['song_name']
                artistName = tabData['artist_name']
                type = tabData['type']
                version = tabData['version']
                votes = tabData['votes']
                rating = tabData['rating']
                date = tabData['date']
                tabUrl = tabData['tab_url']
                tuning = tabData['tuning']
                typeName = tabData['type_name']
                id = tabData['id']

                tab = Tab()
                tab.songTitle = songTitle
                tab.artistName = artistName
                tab.type = type
                tab.version = version
                tab.votes = votes
                tab.rating = rating
                tab.date = date
                tab.tabUrl = tabUrl
                tab.tuning = tuning
                tab.typeName = typeName
                tab.ugId = id

                url = tabUrl.replace('\\', '')
                res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
                if res.status_code != 200:
                    continue
                res.raise_for_status()
                soup = bs4.BeautifulSoup(res.text, 'html.parser')
                results = soup.prettify()

                regex = re.compile('\"content\":(.*?)\}')
                mo = regex.search(results)
                if mo:
                    tab.content = mo.group()
                    payloadTabs.append(tab)

    json_data = json.dumps([ob.__dict__ for ob in payloadTabs])
    TAB_FILE = open('slayerTabsPage1.txt', 'a')
    TAB_FILE.write(json_data)
    TAB_FILE.close()


if len(sys.argv) < 1:
    sys.exit()

artistToSearch = sys.argv[1]

artistUrl = getArtistURL(artistToSearch)

scrapTabs(artistUrl)


sys.exit()

