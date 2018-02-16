# !python3

import bs4
import requests
import sys
import os
import datetime
from selenium import webdriver

def get_district_url(notecards):
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
                                        return url


# first argument is the google OTP key, second is the district to download
if len(sys.argv) > 2:
    otp_key = str(sys.argv[1])
    searchTerms = str(sys.argv[2])

    print(otp_key)
    print(searchTerms)

# searchTerms = 'woodbridge'

goSheetUrl = open("C:\\Users\\steveh.AZEROTH\\Desktop\\goz.html")
soup = bs4.BeautifulSoup(goSheetUrl.read())
notecardsFound = soup.select('div')

url = get_district_url(notecardsFound)
if len(url) > 0:

    # setting download location'
    chromeOptions = webdriver.ChromeOptions()
    downloadLocation = "C:/k/backups"
    prefs = {"download.default_directory" : downloadLocation}
    chromeOptions.add_experimental_option("prefs", prefs)
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

    schemaName = browser.find_element_by_id("schemaName").get_attribute("value")


    backupRows = browser.find_elements_by_class_name('listRowHighlight');
    dataRow = backupRows[0]
    docRow = backupRows[1]

    dataButton = dataRow.find_element_by_class_name('formButtonIcon')
    dataButton.click()

    docButton = docRow.find_element_by_class_name('formButtonIcon')
    docButton.click()

    goodPath = os.path.abspath(downloadLocation)
    os.chdir(goodPath)

    dateTag = str(datetime.date.today())

    pathContents = os.listdir(goodPath)

    # wait until fire is fully downloaded
    while any('crdownload' in dl for dl in pathContents):
        pathContents = os.listdir(goodPath)

    for pathItem in pathContents:
        if dateTag in pathItem:
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


