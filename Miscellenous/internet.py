import urllib.request as req

def connect():
	try:
		req.urlopen('http://google.com')
		return True
	except:
		return False


print('Internet Available' if connect() else 'No Internet Connection Found')