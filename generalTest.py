#coding=utf-8
from __future__ import division
import logging



# [value1,value2]value1表示X出现的概率，value2表示X实际出现的次数

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
	l1=[[1/6,20],[1/6,30],[1/6,12],[1/6,68],[1/6,27],[1/6,39]]
	f=com_kfang(l1,196)
	print f
	