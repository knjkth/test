#coding=utf-8
from __future__ import  division
import logging
import random
from generalTest import com_kfang


'''
间隔检测，	

'''

#startvalue表示起始值，endvalue表示结束值，zone表示整个区间大小，如快3号码范围1-6，zone=6，sequence表示待检测序列,n表示要收集的间隔表格，t表示间隔的长度
#startvalue<=x<endvalue,快3，中下为1<=x<4,中上为3<=x<7
def com_gap(startvalue,endvalue,zone,sequence,n,t):
	logging.basicConfig(format='%(asctime)s %(message)s',filename='test.log',level=logging.DEBUG)
	logging.info('间隔检测开始.....')
	possible=[]
	p=(endvalue-startvalue)/zone

	for i in range(t):
		#possible.append((endvalue-startvalue)*(1-endvalue+startvalue)**i)
		possible.append(p*(1-p)**i)

	#possible.append((1-endvalue+startvalue)**t)
	possible.append((1-p)**t)

	logging.info('possible is %s'% str(possible))

	rnt=[]
	rnt2=[]
	r=0
	s=0
	j=0 #用于记录每次循环i的起始位置
	
	
	logging.info('%d gaps need to collect!' % n)
	for i in range(t+1):
		rnt.append(0)

	

	for i in range(len(sequence)):
		if startvalue<=sequence[i]<endvalue:
			if r<t:
				rnt[r]+=1
				logging.info('length %d has been found,startindex=%d ,endindex=%d,now sequence is %s' %(r,j,i,rnt))
			else:
				rnt[t]+=1
				logging.info('length %d has been found,startindex=%d ,endindex=%d,now sequence is %s' %(r,j,i,rnt))
			r=0
			j=i+1
			s+=1
			if s==n:
				logging.info('间隔表已经收齐')
				break
		else:
			r+=1

	if s<n:
		logging.info('间隔表未收齐')
		logging.info('间隔检测结束....')
		return -1

	logging.info('间隔检测结束....')

	for i in range(t+1):
		rnt2.append([possible[i],rnt[i]])

	return rnt2


def main():
	
	s1=[]
	fj=open('q2_3.txt','r')
	for eachline in fj:
		a1= [int(x) for x in eachline.strip('\n').strip(' ').split(' ')]
		s1.extend(a1)
	fj.close()


	
	exprimentimes=40000

	

	
	lis2=com_gap(1,12,22,s1,exprimentimes,8)

	print lis2

	print com_kfang(lis2,exprimentimes,False)




if __name__ == '__main__':
	main()
	