#coding=utf-8

from __future__ import division
import logging
from random import randrange
from generalTest import com_kfang

print 'test'

def f_jiecheng(n):
	if isinstance(n,int):
		if n>1:
			return n*f_jiecheng(n-1)
		else:
			return 1
	else:
		print '阶乘需要整数参数'

def f_pailie(m,n):
	if isinstance(m,int) and isinstance(n,int):
		if m>=n:
			return f_jiecheng(m)/f_jiecheng(m-n)
		else:
			print '排列输入参数错误,第一个参数要大于第二个参数'
	else:
		print '排列需要整数参数'

def f_zuhe(m,n):
	if isinstance(m,int) and isinstance(n,int):
		if m>=n:
			return f_jiecheng(m)/(f_jiecheng(n)*f_jiecheng(m-n))
		else:
			print '组合输入参数错误,第一个参数要大于第二个参数'
	else:
		print '组合需要整数参数'



def com_coupon(listToTest,rangeNum,rNumber):#listToTest 表示待检测的序列，rangeNum表示序列中不同的元素个数，rNumber表示x想收集的集券长度数量
	logging.basicConfig(format='%(asctime)s %(message)s',filename='test.log',level=logging.DEBUG)
	logging.info('集券测试开始.....')
	logging.info('sequence to be tested is %s' % str(listToTest))
	
	listCouponArray=[]     #标记在一轮集券收集过程中，元素是否出现
	finallyCouponArray=[]  #存储所有的集券数量
	r,q=0,0
	for i in range(rangeNum,rNumber+rangeNum):
		finallyCouponArray.append([i,0])

	if isinstance(rangeNum,int):
		for i in range(rangeNum):
			listCouponArray.append(0)   #集券初始化

	
	for i in range(len(listToTest)):
		if listCouponArray[listToTest[i]-1] == 0:  #字符未出现过
			listCouponArray[listToTest[i]-1]=1     #设定该字符出现
			
			q+=1
			r+=1
			
			if q==rangeNum:       #在这一轮中是否将集券收集齐全
				
				if finallyCouponArray[-1][0]<=r:     #最后一个存储所有大于的情况
					finallyCouponArray[-1][1]+=1
					logging.info('collect length is %d , now all data is: %s' % (r,str(finallyCouponArray)))
					
				else:
					for i in finallyCouponArray:#找到对应集券的长度
						if i[0]==r:
							i[1]+=1    
							break
					logging.info('collect length is %d , now all data is: %s' % (r,str(finallyCouponArray)))
					
				
				r,q=0,0
				for i in range(len(listCouponArray)):
					listCouponArray[i]=0
		
		else:
			r+=1
			
	
	logging.info('集券测试结束.....')						
	return finallyCouponArray


if __name__ == '__main__':
	
	
	sequtest=[]
	possible=[]
	total=0
	
	for i in range(500):
		sequtest.append(randrange(1,7))

	d=6  #表示序列总共有多少个不同的数
	collectnum=5 #表示需要集券的数量
	t=d+collectnum #表示最后一个


	s=com_coupon(sequtest,d,collectnum)
	print s

	for i in range(len(s)):
		total+=s[i][1]    

	r=d
	
	for r in range(r,r+collectnum-1):

		possible.append(f_jiecheng(d)*f_zuhe(r-1,d-1)/pow(d,r))

	possible.append(1-f_jiecheng(d)*f_zuhe(t-1,d)/pow(d,t-1))	

	#print possible
		
	last=[]

	for i in range(len(s)):
		last.append([possible[i],s[i][1]])

	print last	
	
	

	f=com_kfang(last,total,False)
	print f









