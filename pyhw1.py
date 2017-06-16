import re

hand = open('pyhw12.txt')
v = 0
for  line in hand:
	line = line.rstrip()
	n_list = re.findall('[0-9]+', line)
	if len(n_list) > 0:
		for i in n_list:
			v = v + int(i)		
print v

