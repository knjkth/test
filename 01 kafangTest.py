#coding=utf-8
from __future__ import division
import logging 
from random import randrange
from generalTest import com_kfang


#sequence1 表示待统计的序列，sequence2表示范畴，possible表示概率，psIsTrue表示每个范畴的概率是否相等
def com_X(sequence1,sequence2,possible,psIsTrue=True): #若psIsTrue 是真，则possible只要传入一个实数，否则需要传入一个列表
	rtn=[]
	logging.basicConfig(format='%(asctime)s %(message)s',filename='test.log',level=logging.DEBUG)
	logging.info('卡方检验开始.....')
	if psIsTrue==True:
		if isinstance(possible,float):
			for i in sequence2:
				appear=sequence1.count(i)
				rtn.append([possible,appear])
				logging.info('%d has appear %d,  it\'s  possile is %f,now list is %s' %(i,appear,possible,rtn))
		else:
			logging.error('卡方检验传入参数错误，概率应该是一个实数')
			logging.info('卡方检验结束....')
			return -1
	else:
		if isinstance(possible,list) and len(possible)==len(sequence2):
			for i in range(len(sequence2)):
				appear=sequence1.count(sequence2[i])
				rtn.append([possible[i],appear])
				logging.info('%d has appear %d, it\'s  possile is %f, now list is %s' % (i,appear,possible[i],rtn))
		else:
			logging.error('卡方检验传入参数错误，概率不同，需要传入一个列表，且长度与范畴列表长度相同')
			logging.info('卡方检验结束....')
			return -1

	logging.info('卡方检验结束....')
	return rtn



if __name__=='__main__':
	
	s1=[]
	fj=open('number.txt','r')
	for eachline in fj:
		a1= [int(x) for x in eachline.strip('\n').strip(' ').split(' ')]
		s1.extend(a1)
	fj.close()

	print len(s1)

	t=com_X(s1,[1,2,3,4,5,6],1/6)
	print com_kfang(t,len(s1))








	
