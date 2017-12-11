import requests

proxies = {'http': 'http://<<USERID>>:<<PASSWORD>>@23.19.51.245:40791/'}

while True:
	try:
		page = requests.get('http://www.vehiclessellingsolutions.com/', proxies=proxies)
	except Exception as e:
		print(str(e))