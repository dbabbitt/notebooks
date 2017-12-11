import pickle
from random import randint
import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

siteUrl = "http://www.commercialtrucktrader.com/Medium-Duty-Trucks-For-Sale/search-results"
siteUrl = "?".join([siteUrl, "type=medium"])
print(siteUrl)
max_page = 0
seen_urls_array = []

# Retrieve the page with tag results and set it up to be scraped
sitePage = requests.get(url=siteUrl)
sitePageSoup = BeautifulSoup(sitePage.content, 'lxml')

css = 'div.listings-pag-bottom > div > a.listings-pag-default'
pageLinks = sitePageSoup.select(css)
if len(pageLinks):
    max_page = int(pageLinks[-1]["href"].split('=')[2])
print(max_page)

for i in range(1, max_page+1):
    tagUrl = "&".join([siteUrl, "page="+str(i)])
    page = requests.get(url=tagUrl)
    soup = BeautifulSoup(page.content, 'lxml')

    # Get the title of the page to prove we are progressing
    titleTag = soup.select("head > title")
    titleString = titleTag[0].get_text().strip()
    #print(titleString)

    # Get the links to the individual pages
    pageLinks = soup.select('div.listing-header > a > h2')
    for pageLink in pageLinks:
        pageUrl = urllib.parse.urljoin(siteUrl, re.sub(' ', '%20', pageLink.parent['href']))
        #print(pageUrl)
        if pageUrl not in seen_urls_array:
            seen_urls_array.append(pageUrl)
    
    # Destroy the tree when you're done working with it
    soup.decompose()

# Show the number of individual page links you have
print(len(seen_urls_array))

with open('commercialtrucktraderMediumDutyTrucks.pickle', 'wb') as handle:
    pickle.dump(seen_urls_array, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('commercialtrucktraderMediumDutyTrucks.pickle', 'rb') as handle:
    seen_urls_array = pickle.load(handle)

for pageUrl in seen_urls_array:
    try:
        page = requests.get(url=pageUrl)
        soup = BeautifulSoup(page.content, 'lxml')

        dealCss = "body > div.details-container > div.details > div.details-default > div.details-right > strong"
        dealerLink = soup.select(dealCss)
        if len(dealerLink):
            dealerName = dealerLink[0].get_text().strip()

            if dealerName == "Private Seller":
                model = soup.select("div.details > h1")
                if(len(model)):
                    model = model[0].get_text().strip()
                else:
                    model = "Unknown"
                price = soup.select("div.details-right > h2.lfloat")
                if(len(price)):
                    price = price[0].get_text().strip()
                else:
                    price = "Unknown"
                phone = soup.select("span.flipphone.bold.font1-1")
                if len(phone):
                    phone = phone[0].get_text().strip()[::-1]
                else:
                    phone = ""
                if len(phone):
                    bigFile = open('commercialtrucktraderMediumDutyTrucks.txt', 'a', encoding='utf-8')
                    bigFile.write(model + '\t' + price + '\t' + phone + '\n')
                    bigFile.close()
    
        # Destroy the tree when you're done working with it
        soup.decompose()
        
    except Exception as e:
        print(str(e))