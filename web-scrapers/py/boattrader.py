import requests
from bs4 import BeautifulSoup
import re
import pickle
import os

proxies = {'http': 'http://<<USERID>>:<<PASSWORD>>@23.19.51.245:40791/'}
bigFileName = 'boattrader.txt'
os.remove(bigFileName)

with open('boattrader.pickle', 'rb') as handle:
    seen_urls_array = pickle.load(handle)

for pageUrl in seen_urls_array:
    try:
        page = requests.get(url=pageUrl, proxies=proxies)
        soup = BeautifulSoup(page.content, 'lxml')

        #Assume Private Seller
        model = soup.select("header > h1")
        if len(model):
            model = model[0].get_text().strip()
            model = re.sub(r'\s+', ' ', model)
        else:
            model = "Unknown"
        #print(model)
        
        price = soup.select("div.bd-price-location > span")
        if len(price):
            price = price[0].get_text().strip()
        else:
            price = "Unknown"
        #print(price)
        
        phone = soup.select("#call-now-details")
        if len(phone):
            phone = phone[0].get_text().strip()
        else:
            phone = ""
        #print(phone)
        
        if len(phone):
            bigFile = open(bigFileName, 'a', encoding='utf-8')
            bigFile.write(model + '\t' + price + '\t' + phone + '\n')
            bigFile.close()
    
        # Destroy the tree when you're done working with it
        soup.decompose()
        
    except Exception as e:
        print(str(e))