import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
 
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')
sum = 0
for i in tags:
	sum += int(i.contents[0])
print sum
