#coding=utf-8

from __future__ import division
import logging
from random import randrange
from generalTest import com_kfang
import time

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

def s_telin(k,r):
	if r==k and k>=0:
 		return 1
 	elif r==0 and k>=1:
  		return 0
 	else:
  		return r*s_telin(k-1,r)+s_telin(k-1,r-1)


def com_coupon(listToTest,rangeNum,rNumber,totalNumber):#listToTest 表示待检测的序列，rangeNum表示序列中不同的元素个数，
														#rNumber表示集券多少种不同长度的序列,totalNumber表示总共要集券的数量
	logging.basicConfig(format='%(asctime)s %(message)s',filename='test.log',level=logging.DEBUG)
	logging.info('集券测试开始.....')
	#logging.info('sequence to be tested is %s' % str(listToTest))
	
	s=0
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
				s+=1
				if finallyCouponArray[-1][0]<=r:     #最后一个存储所有大于的情况
					finallyCouponArray[-1][1]+=1
					logging.info('the %dth  , collect length is %d , now all data is: %s' % (s,r,str(finallyCouponArray)))
					
				else:
					for t in finallyCouponArray:#找到对应集券的长度
						if t[0]==r:
							t[1]+=1    
							break
					logging.info('the %dth  , collect length is %d , now all data is: %s' % (s,r,str(finallyCouponArray)))
					
				
				r,q=0,0
				for j in range(len(listCouponArray)):
					listCouponArray[j]=0
				
				if s==totalNumber:
					logging.info('当前索引位置是 %d' % (i))
					logging.info('集券收集齐全....')

					break

		
		else:
			r+=1
	
	if s<totalNumber:
		logging.info('集券未收集齐全...')	
		return -1	
	
	logging.info('集券测试结束.....')						
	return finallyCouponArray


if __name__ == '__main__':
	
	
	
	possible=[]

	'''
	possible=[3.292059032949367e-09, 3.4566619845968355e-08, 1.927350924744902e-07,
			   7.588944266183052e-07,2.3682473817678352e-06,6.233962309566002e-06,
			   1.4389023714359412e-05,2.989766602011395e-05, 5.698608262563513e-05,
			   0.00010105294410016535, 0.00016854005990358004, 0.000266666625939972,
			   0.0004030514796139018,0.0005852627896165278, 0.0008203418877349056,
			   0.0011143476568626054,0.0014719615060393614,0.0018961826311083207,
			   0.002388131198489239,0.9906735967503421]

	'''
	
	s1=[]
	fj=open('k3.txt','r')
	for eachline in fj:
		a1= [int(x) for x in eachline.strip('\n').strip(' ').split(' ')]
		s1.extend(a1)
	fj.close()

	d=6  #表示序列总共有多少个不同的数
	collectnum=20#表示需要多少种不同长度的集券数量
	number=20000 #表示总共要收集多少个
	t=d+collectnum-1 #表示最后一个


	s=com_coupon(s1,d,collectnum,number)
	if s!=-1:
		
	
		print s

		
		
		r=d
		
		for x in range(r,r+collectnum-1):
			#tt=time.time()
			#print '%d start, time is:%s' %(x,time.ctime(tt))
			possible.append(f_jiecheng(d)*s_telin(x-1,d-1)/pow(d,x))
			#print '%d is %s,waste %d' %(x,possible,time.time()-tt)


		possible.append(1-f_jiecheng(d)*s_telin(t-1,d)/pow(d,t-1))	

		#print possible
		
		
		last=[]

		for i in range(len(s)):
			last.append([possible[i],s[i][1]])

		print last	
		
		

		f=com_kfang(last,number,False)
		print f

	







