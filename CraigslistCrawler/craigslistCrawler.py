# !python 3

import requests
import bs4

# start logic of loading craigslist page
urlString = "https://cnj.craigslist.org/"
response = requests.get(urlString, headers={'User-Agent': 'Mozilla/5.0'})
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, "html.parser")

