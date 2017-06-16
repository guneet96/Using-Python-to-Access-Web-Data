import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = raw_input('Enter count - ')
posi = raw_input('Enter position - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
print url
for k in range(int(count)):
	j = 0
	for i in tags:
		j+=1
		if j == int(posi):
			url  = i.get('href', None)
			html = urllib.urlopen(url).read()
			soup = BeautifulSoup(html)
			tags = soup('a')
			print i.get('href', None)
			break
		
