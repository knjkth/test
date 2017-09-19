
from socket import *
from time import ctime

host='localhost'
port=10024
addr=(host,port)
buffersize=1024

s1=socket(AF_INET,SOCK_STREAM)

s1.connect(addr)

while True:
	n=raw_input('>')
	if not n:
		break

	s1.send(n)

	n=s1.recv(buffersize)
	if not n:
		break
	print 'i have receive %s' % n

s1.close()
	
