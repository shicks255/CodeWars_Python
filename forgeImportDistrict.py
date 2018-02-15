# !python3

import bs4
import requests
import sys
import os
import datetime
from selenium import webdriver

if len(sys.argv) > 2:
    # address = ' '.join(sys.argv[1:])
    otp_key = str(sys.argv[1])
    searchTerms = str(sys.argv[2])

    print(otp_key)
    print(searchTerms)

# searchTerms = 'woodbridge'

goSheetUrl = open("C:\\Users\\steveh.AZEROTH\\Desktop\\goz.html")

soup = bs4.BeautifulSoup(goSheetUrl.read())

notecards = soup.select('div')

url = ''

for card in notecards:
    if 'notecard' in card.get('class'):
        if 'SchoolFi' in card.find('b').getText():
            districts = card.find_all('tr')
            for district in districts:
                if district.get('data-type'):
                    if 'customer' in district.get('data-type'):
                        if district.find('a'):
                            districtName = district.find('a').getText()
                            if searchTerms.lower() in districtName.lower():
                                if (district.find('a').get('href')):
                                    url = district.find('a').get('href')

if len(url) > 0:

    # setting download location'
    downloadLocation = "C:/k/backups"
    chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument('profile.default_content_settings.popups=0')
    # chromeOptions.add_argument('download.default_directory=C:/k/backups')
    prefs = {"download.default_directory" : downloadLocation}
    chromeOptions.add_experimental_option("prefs", prefs)
    # desiredCapabilities = {'prefs': {'download': {'default_directory': 'C:/k/backups/'}}}
    # path to chromdriver exe
    webdriverPath = "C:/Python\chromedriver.exe"

    browser = webdriver.Chrome(executable_path = webdriverPath, chrome_options = chromeOptions)
    browser.get(url)

    logonField = browser.find_element_by_id("logonid")
    passwordField = browser.find_element_by_id("password")

    # enter credentials here
    logonField.send_keys( "" )
    passwordField.send_keys( "" )

    submit = browser.find_element_by_css_selector("input[type='submit']")

    submit.submit()

    twoFactorPass = browser.find_element_by_id("otp");
    twoFactorPass.send_keys(otp_key)

    submit2 = browser.find_element_by_id("secondFactorForm")
    submit2.submit()

    browser.get(url + "/control?tab1=system&tab2=backups&tab3=files&action=form")

    backupRows = browser.find_elements_by_class_name('listRowHighlight');

    schemaName = browser.find_element_by_id("schemaName").get_attribute("value")
    # schemaName = "sfdunellen"

    dataRow = backupRows[0]
    docRow = backupRows[1]

    dataButton = dataRow.find_element_by_class_name('formButtonIcon')
    dataButton.click()

    docButton = docRow.find_element_by_class_name('formButtonIcon')
    docButton.click()

    goodPath = os.path.abspath(downloadLocation)
    os.chdir(goodPath)

    downloadTag = str(datetime.date.today())

    pathContents = os.listdir(goodPath)

    while any('crdownload' in dl for dl in pathContents):
        pathContents = os.listdir(goodPath)

    for pathItem in pathContents:
        if downloadTag in pathItem:
            if "-docs.dmp.bz2" in pathItem:
                spliceUntil = pathItem.index("-docs.dmp.bz2")
                newName = schemaName + pathItem[spliceUntil:]
                os.rename(pathItem, newName)

            if "-data.dmp.bz2" in pathItem:
                spliceUntil = pathItem.index(".dmp.bz2")
                newName = schemaName + pathItem[spliceUntil:]
                os.rename(pathItem, newName)

    command = "impsfuser " + schemaName
    os.system("start /B start cmd.exe @cmd /k " + command)

    webdriver.close()