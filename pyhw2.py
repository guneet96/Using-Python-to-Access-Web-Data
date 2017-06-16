import socket

mys = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mys.connect(('www.data.pr4e.org', 80))

mys.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
	data = mys.recv(512)
	if len(data) < 1:
		break
	print data
mys.close()
