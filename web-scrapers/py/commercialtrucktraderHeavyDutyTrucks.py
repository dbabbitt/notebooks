import pickle
from bs4 import BeautifulSoup
import urllib.parse
import re
import time

siteUrl = "http://www.commercialtrucktrader.com/Heavy-Duty-Trucks-For-Sale/search-results"
siteUrl = "?".join([siteUrl, "type=heavy"])
print(siteUrl)
max_page = 0
seen_urls_array = []

from selenium import webdriver
from base64 import b64encode

proxy = {'host': '23.19.51.245', 'port': '40791', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>'}
# Retrieve the page with tag results and set it up to be scraped
fp = webdriver.FirefoxProfile()
fp.set_preference('network.proxy.type', 1)
fp.set_preference('network.proxy.http', proxy['host'])
fp.set_preference('network.proxy.http_port', int(proxy['port']))
fp.set_preference('network.proxy.no_proxies_on', 'localhost, 127.0.0.1')
fp.add_extension('closeproxy.xpi')
credentials = '{usr}:{pwd}'.format(**proxy)
credentials = b64encode(credentials.encode('ascii')).decode('utf-8')
fp.set_preference('extensions.closeproxyauth.authtoken', credentials)

#set some privacy settings
fp.set_preference( "places.history.enabled", False )
fp.set_preference( "privacy.clearOnShutdown.offlineApps", True )
fp.set_preference( "privacy.clearOnShutdown.passwords", True )
fp.set_preference( "privacy.clearOnShutdown.siteSettings", True )
fp.set_preference( "privacy.sanitize.sanitizeOnShutdown", True )
fp.set_preference( "signon.rememberSignons", False )
fp.set_preference( "network.cookie.lifetimePolicy", 2 )
fp.set_preference( "network.dns.disablePrefetch", True )
fp.set_preference( "network.http.sendRefererHeader", 0 )

#if you're really hardcore about your security
#js can be used to reveal your true i.p.
fp.set_preference( "javascript.enabled", False )

#get a huge speed increase by not downloading images
fp.set_preference( "permissions.default.image", 2 )

driver = webdriver.Firefox(fp)

# set timeout information
driver.set_page_load_timeout(5)

with open('commercialtrucktraderHeavyDutyTrucks.pickle', 'rb') as handle:
	seen_urls_array = pickle.load(handle)

for pageUrl in seen_urls_array:
    try:
        finished = 0
        while finished == 0:
            try:
                driver.get(pageUrl)
                finished = 1
            except Exception as e:
                print(str(e))
                time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        seller = soup.select('div.details-right > strong')
        if len(seller):
            seller = seller[0].get_text().strip()
        else:
            seller = "Unknown"
        #print(seller)
		
		if seller == "Private Seller":

			model = soup.select("div.details > h1")
			if len(model):
				model = model[0].get_text().strip()
			else:
				model = "Unknown"
			#print(model)

			price = soup.select("div.details-right > h2.lfloat")
			if len(price):
				price = price[0].get_text().strip()
			else:
				price = "Unknown"
			#print(price)

			phone = soup.select("span.flipphone.bold.font1-1")
			if len(phone):
				phone = phone[0].get_text().strip()[::-1]
			else:
				phone = ""
			#print(phone)
			
			if len(phone):
				bigFile = open('commercialtrucktraderHeavyDutyTrucks.txt', 'a', encoding='utf-8')
				bigFile.write(model + '\t' + price + '\t' + phone + '\n')
				bigFile.close()
    
        # Destroy the tree when you're done working with it
        soup.decompose()
        
    except Exception as e:
        print(str(e))