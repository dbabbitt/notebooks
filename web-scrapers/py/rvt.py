
from base64 import b64encode
from bs4 import BeautifulSoup
from random import randint

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import _find_element
from selenium.webdriver.support.ui import WebDriverWait

#import pandas as pd
import pickle
import random
import re
import requests
import time
import urllib.parse

proxies_array = [
    {'host': '64.120.85.192', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'Chicago Ilinois'},
    {'host': '8.29.125.84', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'Columbus Ohio'},
    {'host': '173.234.204.209', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'Dallas Texas'},
    {'host': '8.29.124.215', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'Denver Colorado'},
    {'host': '167.160.106.72', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'Houston Texas'},
    {'host': '192.171.229.113', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'Irvine California'},
    {'host': '45.59.21.72', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'Las Vegas Nevada'},
    {'host': '142.91.235.188', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'Los Angeles California'},
    {'host': '108.62.137.20', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'New York City New York'},
    {'host': '216.107.136.72', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'Oklahoma City Oklahoma'},
    {'host': '23.19.213.86', 'port': '56597', 'usr': '<<USERID>>', 'pwd': '<<PASSWORD>>', 'loc': 'Phoenix Arizona'},
]

def get_firefox_credentials(proxy):
    credentials = '{usr}:{pwd}'.format(**proxy)
    credentials = b64encode(credentials.encode('ascii')).decode('utf-8')
    
    return(credentials)

def get_firefox_profile(proxy, credentials):
    fp = webdriver.FirefoxProfile()
    fp.set_preference('network.proxy.type', 1)
    fp.set_preference('network.proxy.http', proxy['host'])
    fp.set_preference('network.proxy.http_port', int(proxy['port']))
    fp.set_preference('network.proxy.no_proxies_on', 'localhost, 127.0.0.1')
    fp.add_extension('closeproxy.xpi')

    # Set up the credentials
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
    #fp.set_preference( "javascript.enabled", False )

    #get a huge speed increase by not downloading images
    #fp.set_preference( "permissions.default.image", 2 )
    
    return(fp)

def get_firefox_page(proxy, url):
    credentials = get_firefox_credentials(proxy)
    fp = get_firefox_profile(proxy, credentials)
    driver = webdriver.Firefox(fp)

    # Set the timeout information
    driver.set_page_load_timeout(50)

    finished = 0
    fails = 0
    while finished == 0 and fails < 8:
        try:
            driver.get(url)
            finished = 1
        except Exception as e:
            print(str(e))
            fails = fails + 1
            time.sleep(5)
    
    return(driver)

class text_to_change(object):
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        actual_text = _find_element(driver, self.locator).text
        return actual_text != self.text

siteUrl = "http://www.rvt.com/New-and-Used-RVs-For-Sale-On-RVT.com/results"
siteUrl = "?".join([siteUrl, "private_only=1"])
print(siteUrl)

# Retrieve the page with tag results and set it up to be scraped
proxy = proxies_array[randint(0, len(proxies_array)-1)]
proxy_url = 'http://{usr}:{pwd}@{host}:{port}/'.format(**proxy)
sitePage = requests.get(url=siteUrl, proxies={'http': proxy_url})
siteSoup = BeautifulSoup(sitePage.content, 'lxml')

links = siteSoup.select('div.result-col > div.post-search > ul > li > a')
print(sitePage.content)
max_page = int(links[-2]['href'].split('=')[-1])
print(max_page)

unseen_urls_array = []

try:
    with open('rvt.pickle', 'rb') as handle:
        seen_urls_array = pickle.load(handle)
except Exception as e:
    print(str(e))
    seen_urls_array = []

for i in range(1, max_page+1):
    url = siteUrl+"&page="+str(i)

    # Retrieve the page with tag results and set it up to be scraped
    proxy = proxies_array[randint(0, len(proxies_array)-1)]
    proxy_url = 'http://{usr}:{pwd}@{host}:{port}/'.format(**proxy)
    page = requests.get(url=url, proxies={'http': proxy_url})
    soup = BeautifulSoup(page.content, 'lxml')
    
    # Get links
    pageLinks = soup.find_all("a", class_="result-link")
    for pageLink in pageLinks:
        pageUrl = urllib.parse.urljoin(url, re.sub(' ', '%20', pageLink['href']))
        if pageUrl not in unseen_urls_array:
            unseen_urls_array.append(pageUrl)

unseen_urls_array = list(set(unseen_urls_array) - set(seen_urls_array))
seen_urls_array = []
scrambled_urls_array = sorted(unseen_urls_array, key = lambda x: random.random())
for url in scrambled_urls_array:

    # Get random proxy
    proxy = proxies_array[randint(0, len(proxies_array)-1)]
    #print(proxy['loc'])

    driver = get_firefox_page(proxy, url)
    
    phoneRe = re.compile(r"\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}")

    # Get the "Click to Show"
    phoneID = 'sc1'
    try: 
        text_before = driver.find_element_by_id(phoneID).text 
    except NoSuchElementException: 
        text_before = ""
    #print("text_before: '" + text_before + "'")

    try:

        # Wait for the button to show up
        #<a href="#contact-seller">Call<br>Seller</a>
        buttonCss = 'li.call-seller-pr > a[href="#contact-seller"]'
        buttonTag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, buttonCss))
        )
        buttonTag.click()

        # Wait for the phone number to show up
        WebDriverWait(driver, 10).until(
            text_to_change((By.ID, phoneID), text_before)
        )
        pageSoup = BeautifulSoup(driver.page_source, 'lxml')

        phoneTag = pageSoup.select('span.show-phone > a')
        if(len(phoneTag)):
            match = phoneRe.search(phoneTag[0].get_text().strip())
            if match:
                phone = match.group()
            else:
                phone = ""
        else:
            phone = ""
        #print("phone: '" + phone + "'")

        if len(phone):

            modelCss = "div.detail-header > h1"
            model = pageSoup.select(modelCss)
            if(len(model)):
                model = model[0].get_text().strip()
            else:
                model = "Unknown"
            #print("model: '" + model + "'")

            priceCss = 'li.bold > span.rv-item-data'
            priceTag = pageSoup.select(priceCss)
            if(len(priceTag)):
                price = priceTag[0].get_text().strip()
            else:
                price = "Unknown"
            #print("price: '" + price + "'")

            bigFile = open('rvt.txt', 'a', encoding='utf-8')
            bigFile.write(model + '\t' + price + '\t' + phone + '\n')
            bigFile.close()

        # Destroy the tree when you're done working with it
        pageSoup.decompose()

    except Exception as e:
        print(str(e))
    finally:
        if url not in seen_urls_array:
            seen_urls_array.append(url)
        try:
            with open('rvt.pickle', 'wb') as handle:
                pickle.dump(seen_urls_array, handle, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print(str(e))
        try:
            driver.quit()
        except Exception as e:
            print(str(e))