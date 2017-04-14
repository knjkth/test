from time import sleep,ctime
import threading
import Queue
from random import randrange
import linecache





def tongji(position,fj,linetoread,s):
	total=0
	fj.seek(0,0)
	for i in range(position-1):
		fj.next()

	for i in range(linetoread):
		p=[int(x) for x in fj.next().strip('\n').strip().split(' ')]
				
		for i in range(len(p)):
			if p[i]==s:
				total+=1

	return total
	


def main():
	totallines=0
	div=10
	fj=open('test.txt')

	for i in fj:
		totallines+=1

	fj.seek(0,0)

	lthread=[]
	position=[]

	for i in range(10)


	for i in range(10):
		threading.Thread(tongji,())





fj.close()