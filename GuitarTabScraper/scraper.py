# !python3
import re

import bs4
import requests

# this is the URl that will print a list of search results
url = 'https://www.ultimate-guitar.com/search.php?search_type=title&value='
# url = 'https://www.ultimate-guitar.com/artist/slayer_459'
artistQuery = 'Slayer'
artistQuery = artistQuery.lower()

res = requests.get(url+artistQuery, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
results = soup.prettify()

# start = results.find('{\"artist_name\":')
# end = results.find('header_bidding')
# results = results[start:end]

# to get the tabs
# regex = re.compile('(\{\"id\":)(.*?)((\]\}\}))')
# to get the artist url when searching for artist
regex = re.compile('artist/(.*?)\"')
mo = regex.search(results)

if mo:
    print(mo.groups())







