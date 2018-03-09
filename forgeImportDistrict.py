# !python3

import datetime
import os
import sys
import time
import pyperclip

import bs4
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
    searchTerms = ' '.join(sys.argv[2:])
    # numberOfSearchTerms = len(sys.argv)
    # search = numberOfSearchTerms - 2
    # searchTerms = ''
    # for i in range(search, numberOfSearchTerms, 1):
    #     searchTerms = searchTerms + ' ' + sys.argv[i]

    print(otp_key)
    print(searchTerms)

if len(sys.argv) < 2:
    print('Run the program again in the form of - load [OTP_KEY] [DISTRICT NAME]')
    sys.exit()

# Location of Go sheet
goSheetUrl = open("C:\\Users\\steveh.AZEROTH\\Desktop\\goz.html")
soup = bs4.BeautifulSoup(goSheetUrl.read())
notecardsFound = soup.select('div')

url = get_district_url(notecardsFound)
if not url:
    print('No district found')
    sys.exit()
if len(url) > 0:

    # setting download location
    chromeOptions = webdriver.ChromeOptions()
    downloadLocation = "C:/k/backups"
    prefs = {"download.default_directory" : downloadLocation}
    chromeOptions.add_experimental_option("prefs", prefs)
    webdriverPath = "C:/Python\chromedriver.exe"

    # Create Selenium WebDriver
    browser = webdriver.Chrome(executable_path = webdriverPath, chrome_options = chromeOptions)
    browser.get(url)

    # wait a second
    time.sleep(1)

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

    # cleaning up the URLs of some non-ASP customers
    if "schoolfi" not in url:
        if url[-1] == "/":
            url = url + "schoolfi"
        else:
            url = url + "/schoolfi"
    browser.get(url + "/control?tab1=system&tab2=backups&tab3=files&action=form")

    backupRows = browser.find_elements_by_class_name('listRowHighlight');
    dataRow = backupRows[0]
    docRow = backupRows[1]

    dataButton = dataRow.find_element_by_class_name('formButtonIcon')
    dataButton.click()

    docButton = docRow.find_element_by_class_name('formButtonIcon')
    docButton.click()

    goodPath = os.path.abspath(downloadLocation)
    os.chdir(goodPath)

    # get schema name and copy to clipboard for context.xml file
    schemaName = browser.find_element_by_id("schemaName").get_attribute("value")
    pyperclip.copy(schemaName)
    dateTag = str(datetime.date.today())

    pathContents = os.listdir(goodPath)

    # wait until file is fully downloaded
    while any('crdownload' in dl for dl in pathContents):
        pathContents = os.listdir(goodPath)

    time.sleep(2)

    browser.close()
    browser.quit()

    # deleting the 2 old files if they exists
    oldData = schemaName + ".dmp"
    oldDocs = schemaName + "-docs.dmp"
    if any(oldDocs in docsFile for docsFile in os.listdir(goodPath)):
        os.remove(oldDocs)
    if any(oldData in file for file in os.listdir(goodPath)):
        os.remove(oldData)

    # renaming the files to SCHEME.dmp.bz2/-docs.dmp.bz2
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
