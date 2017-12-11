from selenium import webdriver
from base64 import b64encode

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

def get_proxies_array():
	return (get_proxies_array)

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
			driver.get(siteUrl)
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