#encoding=utf-8

from generalTest import com_kfang
import random
import logging
import itertools
'''
序列检测
多元组检测（至少2个元素），统计每个范畴实际出现的次数，再进行卡方检测。
'''

def k3(): #产生快3基础数据
	rg=6
	base=[]
	for i in range(rg):
		for j in range(rg):
			for k in range(rg):
				base.append((i+1,j+1,k+1))
	return base


def P125(): #产生12选5基础数据
	return tuple(itertools.combinations([1,2,3,4,5,6,7,8,9,10,11,12],5))


def comp_sequence(lisToCheck,allPossbileValue,fan): #lisToCheck表示需要比对的原始数据，allPossbileValue表示所有比对可能的值,fan表示元组的个数，如2表示2元组
	if isinstance(allPossbileValue,tuple):
		templist=list(allPossbileValue)
	else:
		templist=allPossbileValue
	dictToSave={}
	
	logging.basicConfig(format='%(asctime)s %(message)s',filename='test.log',level=logging.DEBUG)
	logging.info('序列检测开始....')
	for i in range(len(lisToCheck)/fan):
		tlist=[] #临时存储比对对象
		for  tkey in range(fan):
				tlist.append(lisToCheck[fan*i+tkey])

		
		for key,value in enumerate(templist):
		
			if tuple(tlist)==value:
				if key in dictToSave:    #如果在字典中，则加1
					dictToSave[key]+=1
					
				else:               #如果原来字典中没有，则赋值为1
					dictToSave[key]=1
					
				break

	for key,value in dictToSave.items():
		logging.info('%s value is %d' %(templist[key],value))

	logging.info('序列检测结束....')
	return dictToSave  #key表示allPossbileValue对应的索引，value表示出现的次数



if __name__ == '__main__':
	
	logging.basicConfig(format='%(asctime)s %(levelname)s : %(message)s ',filename='test.log',level=logging.DEBUG)
	s1=[]
	list2=[]

	fj=open('k3.txt','r')
	for eachline in fj:
		a1= [int(x) for x in eachline.strip('\n').strip(' ').split(' ')]
		s1.extend(a1)
	fj.close()

	
	
	logging.info('sequence to be tested is :%s' % str(s1))



	tuple1=tuple(k3())

	print tuple1


	t=comp_sequence(s1,tuple1,3)

	
	
	for value in t.values():
		list2.append([1.0/216,value])
		
	

	f=com_kfang(list2,len(s1)/3)
	print f







	
	

	

	

