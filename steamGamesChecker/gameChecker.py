import requests
import bs4
import re
import json
import os
import sys
import datetime

url = 'https://steamcommunity.com/id/kpad/games/?tab=all'
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

regex = re.compile('(rgGames)(.*?)(}}])')
mo = regex.search(res.text)

if mo:
    payload = str(mo.groups()[1]) + str(mo.groups()[2])
    startJson = payload.index('[')
    payload = payload[startJson:]

    payload = payload.replace('\\\\', '')
    payload = payload.replace('\\', '')
    try:
        games = json.loads(payload)
    except json.decoder.JSONDecodeError:
        print('error with making json')

    os.chdir(sys.path[0])
    LOG_FILE = open('gamesFile.txt', 'a')

    for game in games:
        appId = str(game['appid'])
        name = game['name']
        line = name + ' - ' + appId
        if line not in open('gamesFile.txt').read():
            LOG_FILE.write(line + ' ' + datetime.datetime.now().strftime('%m-%d-%y %H:%M:%S:%f%p'))
            LOG_FILE.write('\n')

    LOG_FILE.close()
    sys.exit()