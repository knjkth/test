#coding=utf-8
from __future__ import  division
import logging
from random import randrange
from generalTest import *


def jiechen(d,r):  #d表示阶乘的起始数，r表示要乘几次，结果=d*(d-1)*(d-2)*..*(d-r+1),当d=r时，表示d的阶乘
	t=d-r
	def jiechen2(x):
		if x==t:
			return 1
		return x*jiechen2(x-1)
	return jiechen2(d)
	


def com_possible(d,k=5):#n表示总共有多少个概率值，d表示随机数的范围,k表示几元组(也表示总共有多少个概率值)，默认为5
	possilbe=[]
	for i in range(1,k+1):
		possilbe.append(jiechen(d,i)*f_zuhe(k,i)/pow(d,k))
	return possilbe


def com_differ_number(list5number): #计算一个五元组中有多少个不同
	
	lisave=[]
	length=len(list5number)
	for i in range(1,length):
		temp=int(list5number[0])-int(list5number[i])
		if temp!=0 and temp not in lisave:
			lisave.append(temp)
	return len(lisave)+1   #加1表示算上自己，也就是list5number[0]这个数


def com_puke(listtotest,d,n=5):#listtotest 表示待检测的序列，d表示随机数范围，n表示按几元组来检测，默认为5
	logging.basicConfig(format='%(asctime)s %(message)s',filename='test.log',level=logging.DEBUG)
	logging.info('扑克检验开始.......')
	length=int(len(listtotest)/n)
	result=[0]*n
	rnt=[]
	for i in xrange(length):
		logging.info('the %d sequence to be tested is %s' % (i+1,listtotest[n*i:n*i+n]))
		t=com_differ_number(listtotest[n*i:n*i+n])
		result[t-1]+=1
		logging.info('current restult is %s' % result )
	logging.info('扑克检验结束.....')

	possible=com_possible(d,n)

	for i in range(n):
		rnt.append([possible[i],result[i]])


	return (length,rnt)  #返回总执行次数及执行结果


def main():
	
	sequtest=[]
	for i in range(50000):
		sequtest.append(randrange(1,7))
	n,s2=com_puke(sequtest,7)

	print n,s2
	print com_kfang(s2,n,False)




if __name__ == '__main__':
	main()
	


