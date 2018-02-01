# !python3

import webbrowser
import sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

    url = "https://www.google.com/maps/search/"

    searchTerms = address.split()

    count = 0
    for searchTerm in searchTerms:
        if count > 0:
            url += "+" + searchTerm
        if count == 0:
            count += 1
            url += searchTerm

    webbrowser.open(url)
