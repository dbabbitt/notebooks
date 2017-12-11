siteUrl = "http://www.trade-a-plane.com/filtered/search"
siteUrl = "?".join([siteUrl, "s-type=aircraft"])
siteUrl = "&".join([siteUrl, "s-keyword-search="])
print(siteUrl)

proxies = {'http': 'http://<<USERID>>:<<PASSWORD>>@23.19.51.245:40791/'}

import requests
from bs4 import BeautifulSoup

# Retrieve the page with tag results and set it up to be scraped
sitePage = requests.get(url=siteUrl, proxies=proxies)
siteSoup = BeautifulSoup(sitePage.content, 'lxml')

#<a href="/search?s-type=aircraft&amp;s-keyword-search=&amp;s-page=137"> &gt;&gt; </a>
siteLinks = siteSoup.select('a[href*=s-page]')
#print(siteLinks)

# Get the max page link
max_page = 0
if len(siteLinks):
    max_page = int(siteLinks[-1]['href'].split('=')[-1])
print(max_page)

import re

for i in range(1, max_page+1):
    tagUrl = "&".join([siteUrl, "s-page="+str(i)])

    tagPage = requests.get(url=tagUrl, proxies=proxies)
    tagSoup = BeautifulSoup(tagPage.content, 'lxml')
    
    phoneLinks = tagSoup.select('span[itemprop="telephone"]')
    for phoneLink in phoneLinks:
        
        phone = phoneLink.get_text().strip()
        if len(phone):

            phoneSoup = phoneLink.parent.parent.parent.parent.parent
            
            seller = phoneSoup.select('a[itemprop="name"]')
            if(len(seller)):
                seller = seller[0].get_text().strip()
                seller = re.sub(r'\s+', ' ', seller)
            else:
                seller = "Unknown"

            model = phoneSoup.select('#title')
            if(len(model)):
                model = model[0].get_text().strip()
                model = re.sub(r'\s+', ' ', model)
            else:
                model = "Unknown"

            price = phoneSoup.select('ul.result_header > li.price')
            if(len(price)):
                price = price[0].get_text().strip()
            else:
                price = "Unknown"
            
            bigFile = open('trade-a-plane.txt', 'a', encoding='utf-8')
            bigFile.write(seller + ': ' + model + '\t' + price + '\t' + phone + '\n')
            bigFile.close()