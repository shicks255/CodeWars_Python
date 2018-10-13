# !python3
import re

import bs4
import requests

# this is the URl that will print a list of search results
url = 'https://www.ultimate-guitar.com/search.php?search_type=title&value='
artistQuery = 'Slayer'
artistQuery = artistQuery.lower()

res = requests.get(url+artistQuery, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
results = soup.prettify()

start = results.find('{\"artist_name\":')
end = results.find('header_bidding')
results = results[start:end]

regex = re.compile('\{"id":.*\]\}\}')
mo = regex.findall(results)

print(results)
# class that is in the search results 'link-secondary _1kcZ5'

# artistSearchResults = soup.findAll('a', {'class':['link-secondary', '_1kcZ5']})
artistSearchResults = soup.find_all('tab_url')
print(artistSearchResults)
for x in artistSearchResults:
    print(x)

