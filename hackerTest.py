# !python3

import sys
import webbrowser
import requests
import bs4

# if len(sys.argv[1:] > 0):
#     url = ' '.join(sys.argv[1:])

url = 'http://ipexclusivity.com/wp-admin'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

loginForm = soup.select('form[name="loginform"]')

print(type(loginForm))
print(len(loginForm))
print(str(loginForm[0]))
print(loginForm[0].get_text)


# http://ipexclusivity.com/wp-admin