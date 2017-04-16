from time import sleep,ctime
import threading
import Queue
from random import randrange
import linecache



tt=0

def tongji(position,name,linetoread,s,name2):
	
	fj=open(name,'r')

	print '%s starting:%s' % (name2,ctime())
	total=0
	
	for i in xrange(position-1):
		fj.next()

	for i in xrange(linetoread):
		p=[int(x) for x in fj.next().strip('\n').strip().split(' ')]
		total+=p.count(s)

	global tt
	tt+=total
	#print 'total is:%d' % total
	print '%s ending:%s' % (name2,ctime())

	fj.close()

	return total
	


def main():
	totallines=0
	div=20
	filename='number.txt'
	
	
	fj=open(filename,'r')

	for i in fj:
		totallines+=1

	fj.close()
	

	lthread=[]
	position=[]
	linetoread=[]

	for i in xrange(div):
		position.append(i*(totallines/div))

	for i in xrange(div-1):
		linetoread.append(totallines/div)

	linetoread.append(totallines-(div-1)*(totallines/div))

	

	for i in range(div):
		t=threading.Thread(target=tongji,args=(position[i],filename,linetoread[i],5,'p'+str(i)))
		lthread.append(t)


	for i in lthread:
		i.start()

	for i in lthread:
		i.join()

	



if __name__ == '__main__':
	main()
	print 'tt is %d' % tt


#fj.close()