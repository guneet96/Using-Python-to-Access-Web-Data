import json
import urllib


base_url = 'http://python-data.dr-chuck.net/geojson?'

while True:
	address = raw_input('Enter - ')
	if len(address) < 1:
		print 'Please enter something...'
		continue
	
	url = base_url + urllib.urlencode({"sensor" : "false", "address" : address})
	data = urllib.urlopen(url).read()
	print data
	
	try:
		js = json.loads(str(data))
	except:
		js = None
	if 'status' not in js or js['status'] != 'OK':
		print '-------Failed to Retrieve-------'
		print data
		continue
	place_id = js["results"][0]["place_id"]
	print place_id
