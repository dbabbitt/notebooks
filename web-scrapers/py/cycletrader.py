import pickle

with open('cycletrader.pickle', 'rb') as handle:
    seen_urls_array = pickle.load(handle)
	
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import zipfile

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "23.19.51.245",
            port: parseInt(40791)
          },
          bypassList: ["foobar.com"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "<<USERID>>",
            password: "<<PASSWORD>>"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
"""


pluginfile = 'proxy_auth_plugin.zip'

with zipfile.ZipFile(pluginfile, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)

co = Options()
co.add_argument("--start-maximized")
co.add_argument('--dns-prefetch-disable')
co.add_extension(pluginfile)

import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

phoneRe = re.compile(r"\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}")
for pageUrl in seen_urls_array:
    try:
        driver = webdriver.Chrome(chrome_options=co)

        # Set timeout information
        driver.set_page_load_timeout(50)

        # Bring up the page
        finished = 0
        fails = 0
        while finished == 0 and fails < 8:
            try:
                driver.get(pageUrl)
                finished = 1
            except Exception as e:
                print(str(e))
                fails = fails + 1
                time.sleep(5)

        # Click the phone button
        try:
            buttonCss = "div.seller-info-telephone > button"

            # Wait for button to show up
            buttonTag = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, buttonCss))
            )

            buttonTag.click()
        except Exception as e:
            print(str(e))

        # Get the phone number
        phoneCss = 'div.sellerOverview > div.seller-info-telephone'

        # Wait for button to disappear
        WebDriverWait(driver, 30).until_not(
            EC.visibility_of_element_located((By.CSS_SELECTOR, buttonCss))
        )

        phoneHTML = driver.find_element_by_css_selector(phoneCss).get_attribute('innerHTML')
        match = phoneRe.search(phoneHTML)
        if match:
            phone = match.group()
        else:
            phone = ""
        #print(phone)

        if len(phone):

            model = driver.find_element_by_css_selector("div.detail-title.lfloat > h1").text.strip()
            if len(model):
                model = re.sub(r'\s+', ' ', model)
            else:
                model = "Unknown"
            #print(model)

            price = driver.find_element_by_css_selector("div.detail-price.rfloat > h2 > span").text.strip()
            if not len(price):
                price = "Unknown"
            #print(price)

            bigFile = open('cycletrader.txt', 'a', encoding='utf-8')
            bigFile.write(model + '\t' + price + '\t' + phone + '\n')
            bigFile.close()

        else:
            print(phoneHTML)
            driver.save_screenshot('cycletrader.png')

    except Exception as e:
        print(str(e))
    finally:
        driver.quit()