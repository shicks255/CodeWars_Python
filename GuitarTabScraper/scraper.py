# !python3
import re
import sys
import psycopg2

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
    artistName = artistName.replace(' ', '%20')
    res = requests.get(MAIN_URL + 'search.php?search_type=band&value=' + artistName)
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
                thisArtistUrl = x[thisArtistUrlIndex+15 : x.find('\"tabs_cnt\"')-2]
                print(thisArtistUrl)


# this is where the heavy lifting is done, remember to add CHORDS
def scrapTabs(artistUrl, pageNumber):
    artistUrl = MAIN_URL + 'artist/' + artistUrl + '?pageNumber=' + pageNumber + '?filter=tabs'

    res = requests.get(artistUrl, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    results = soup.prettify()

    payloadTabs = []

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
            tabData = json.loads(tab)
            # print('\r\n')
            # print(tabData)
            # print(tabData['song_name'] + ' ' + tabData['tab_url'])
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
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            results = soup.prettify()

            regex = re.compile('\"content\":(.*?)\}')
            mo = regex.search(results)
            if mo:
                tab.content = mo.group()

                payloadTabs.append(tab)

        TAB_FILE = open('slayerTabsPage1.html', 'a')

        try:
            conn = psycopg2.connect(host="localhost", database="guitarTabs", user="postgres", password="ashley")
            cursor = conn.cursor()
            # cursor.execute("select version()")
            # data = cursor.fetchone()

            for t in payloadTabs:

                sql = 'insert into tab(artist, title, content, author_id) values(%s,%s,%s,%s) ;'
                cursor.execute(sql, (t.artistName, t.songTitle, t.content, t.ugId))

                TAB_FILE.write('<h3>Artist: '  + t.artistName + '</h3>')
                TAB_FILE.write('<h4>Song: ' + t.songTitle + '</h4>')
                TAB_FILE.write('<div style="white-space: pre-wrap;">' + t.content + '</div>')
                TAB_FILE.write('<br/>')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close();

        TAB_FILE.close()

if len(sys.argv) < 1:
    sys.exit()

artistToSearch = sys.argv[1]

artistUrl = getArtistURL(artistToSearch)


sys.exit()

