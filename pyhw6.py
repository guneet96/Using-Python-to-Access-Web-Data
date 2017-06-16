import urllib
import json

url = raw_input('Enter - ')
if len(url) < 1:
	print 'Please enter some URL...'

data = urllib.urlopen(url).read()
js= json.loads(str(data))
s = 0
j = 0
for i in js["comments"]:
	s += int(js["comments"][j]["count"])
	j+=1
print s

