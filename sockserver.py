
from socket import *
from time import ctime


host=''
port=10001
addr=(host,port)
buffersize=1024

sockser=socket(AF_INET,SOCK_STREAM)

sockser.bind(addr)

sockser.listen(5)

while True:
	print 'i am waiting for sb...'
	sockanother,addr=sockser.accept()
	print '%s has connected' % str(addr)

	while True:
		content=sockanother.recv(buffersize)
		if not content:
			break
		sockanother.send('[%s] has received at %s' % (content,ctime()))
	sockanother.close()
	
		
