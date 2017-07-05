#coding=utf-8
from __future__ import division
import logging


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


# [value1,value2]value1表示X出现的概率，value2表示X实际出现的次数
#listToCompu表示待检测的序列，exprimentNumber表示实验的总次数
def com_kfang(listToCompu,exprimentNumber,psIsTrue=True):  #psIsTrue表示默认情况下每个X出现的概率相等
	sum=0
	kafang=0.0
	
	logging.basicConfig(format='%(asctime)s %(message)s',filename='test.log',level=logging.DEBUG)
	if isinstance(listToCompu,list) and isinstance(exprimentNumber,int):
		length=len(listToCompu)

		for i in range(length):
			sum+=listToCompu[i][1]      #对所有实验次数求和，校验总和是否正确

		if sum!=exprimentNumber:
			logging.error('卡方计算实验次数校验失败')
			return -1
		else:
			sum=0
			logging.info('卡方计算开始.....')

			if psIsTrue==True:
				possible=listToCompu[0][0]
				for k in range(length):
					sum+=listToCompu[k][1]**2
					logging.info('sum value is %f' % sum)
				try:

					kafang = sum*(1.0/exprimentNumber)*(1.0/possible)-exprimentNumber
					logging.info('kafang value is %f' % kafang)
					logging.info('卡方计算结束.....')
					return kafang
				except ZeroDivisionError:
					logging.error('卡方计算发生了除零错误')
					return -1

				
			else:
				try:
					for k in range(len(listToCompu)):
						sum+=(listToCompu[k][1]**2)/listToCompu[k][0]
						logging.info('sum value is %f' % sum) 
					kafang = ((1.0/exprimentNumber)*sum)-exprimentNumber
					logging.info('kafang value is %f' % kafang)
					logging.info('卡方计算结束.....')
					return kafang

				except ZeroDivisionError:
					logging.error('卡方计算发生了除零错误')
					return -1

	else:
		logging.error('调用卡方计算参数错误')
		return -1





if __name__ == '__main__':
	count1=0
	count2=0
	count3=0
	count4=0
	count5=0
	count6=0
	fj=open('data.dat','r')
	for eachline in fj:
		count1+=eachline.strip('\n').count('1')
		count2+=eachline.strip('\n').count('2')
		count3+=eachline.strip('\n').count('3')
		count4+=eachline.strip('\n').count('4')
		count5+=eachline.strip('\n').count('5')
		count6+=eachline.strip('\n').count('6')

	total=count1+count2+count3+count4+count5+count6
	l1=[[1/6,count1],[1/6,count2],[1/6,count3],[1/6,count4],[1/6,count5],[1/6,count6]]
	print l1,total
	
	f=com_kfang(l1,total)
	print f
	