from selenium import webdriver
from base64 import b64encode
import selenium.webdriver.support.ui as ui
import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

siteUrl = "https://www.cars.com/for-sale/searchresults.action/"
siteUrl = "?".join([siteUrl, "perPage=50"])
siteUrl = "&".join([siteUrl, "rd=99999"])
siteUrl = "&".join([siteUrl, "searchSource=UTILITY"])
siteUrl = "&".join([siteUrl, "sf1Dir=DESC"])
siteUrl = "&".join([siteUrl, "sf1Nm=price"])
siteUrl = "&".join([siteUrl, "sf2Dir=ASC"])
siteUrl = "&".join([siteUrl, "sf2Nm=miles"])
siteUrl = "&".join([siteUrl, "slrTypeId=28879"])
siteUrl = "&".join([siteUrl, "sortFeatures=buryLowPriceOlderThanSix"])
siteUrl = "&".join([siteUrl, "sortFeatures=buryNewLowPrice"])
siteUrl = "&".join([siteUrl, "sortFeatures=buryNoPrice"])
siteUrl = "&".join([siteUrl, "sortFeatures=buryUsedLowMileage"])
siteUrl = "&".join([siteUrl, "sortFeatures=buryUsedLowPrice"])
siteUrl = "&".join([siteUrl, "stkTypId=28881"])
siteUrl = "&".join([siteUrl, "yrId=20141"])
siteUrl = "&".join([siteUrl, "yrId=20142"])
siteUrl = "&".join([siteUrl, "yrId=20143"])
siteUrl = "&".join([siteUrl, "yrId=20144"])
siteUrl = "&".join([siteUrl, "yrId=20145"])
siteUrl = "&".join([siteUrl, "yrId=20180"])
siteUrl = "&".join([siteUrl, "yrId=20197"])
siteUrl = "&".join([siteUrl, "yrId=20198"])
siteUrl = "&".join([siteUrl, "yrId=20199"])
siteUrl = "&".join([siteUrl, "yrId=20200"])
siteUrl = "&".join([siteUrl, "yrId=20201"])
siteUrl = "&".join([siteUrl, "yrId=27381"])
siteUrl = "&".join([siteUrl, "yrId=34923"])
siteUrl = "&".join([siteUrl, "yrId=39723"])
siteUrl = "&".join([siteUrl, "yrId=47272"])
siteUrl = "&".join([siteUrl, "yrId=51683"])
siteUrl = "&".join([siteUrl, "yrId=56007"])
siteUrl = "&".join([siteUrl, "yrId=58487"])
siteUrl = "&".join([siteUrl, "zc=60606"])
#print(siteUrl)

proxies = {'http': 'http://<<USERID>>:<<PASSWORD>>@23.19.51.245:40791/'}

sitePage = requests.get(url=siteUrl, proxies=proxies)
sitePageSoup = BeautifulSoup(sitePage.content, 'lxml')
srp_header = sitePageSoup.select('h1.srp-header')
max_page = 0
if len(srp_header):
    max_record_string = srp_header[0].get_text().strip()
    print(max_record_string)
    max_record = int(re.sub('\\D+', '', max_record_string))
    max_page = round(max_record/50)
    print(str(max_page) + " Pages")

for i in range(1, max_page+1):
    tagPageUrl = siteUrl+"&page="+str(i)
    print("Page " + str(i))
    bigFile = open('cars.txt', 'a', encoding='utf-8')
    bigFile.write(tagPageUrl + '\n')
    bigFile.close()

    # Retrieve the page with tag results and set it up to be scraped
    tagPage = requests.get(url=tagPageUrl, proxies=proxies)
    tagPageSoup = BeautifulSoup(tagPage.content, 'lxml')

    links = tagPageSoup.find_all("a", class_="listing-row__photo")
    numLinks = 0
    totalLinks = len(links)
    for link in links:
        url = urllib.parse.urljoin(tagPageUrl, re.sub(' ', '%20', link['href']))
        page = requests.get(url=url, proxies=proxies)
        soup = BeautifulSoup(page.content, 'lxml')
        
        dealer_css = 'h4.dealer-name.cui-delta > span'
        dealer_link_text = "Private Seller"
        dealer_link = soup.select(dealer_css)
        is_dealer = False
        if len(dealer_link):
            match = re.search(dealer_link_text, dealer_link[0].get_text().strip())
            if match:
                is_dealer = False
            else:
                is_dealer = True
        else:
            is_dealer = True
        if not is_dealer:

            model = soup.find_all("h1", class_="vdp-header__title")
            if(len(model)):
                model = model[0].get_text().strip()
            else:
                model = "Unknown"
            #print(model)

            price = soup.find_all("strong", class_='vdp-header__price--primary')
            if(len(price)):
                price = price[0].get_text().strip()
            else:
                price = "Unknown"
            #print(price)

            phone_css = 'span.phone > span > span'
            phone = soup.select(phone_css)
            if(len(phone)):
                phone = phone[0].get_text().strip()
            else:
                phone = ""
            #print(phone)
            if(len(phone)):
                bigFile = open('cars.txt', 'a', encoding='utf-8')
                bigFile.write(model + '\t' + price + '\t' + phone + '\n')
                bigFile.close()
                numLinks = numLinks + 1
    message = str(numLinks) + ' out of ' + str(totalLinks) + ' links\n\n'
    bigFile = open('cars.txt', 'a', encoding='utf-8')
    bigFile.write(message)
    bigFile.close()
    print(message)