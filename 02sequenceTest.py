#encoding=utf-8

from generalTest import com_kfang
import random
import logging




def comp_sequence(lisToCheck,allPossbileValue): #lisToCheck表示需要比对的原始数据，allPossbileValue表示所有比对可能的值
	if isinstance(allPossbileValue,tuple):
		templist=list(allPossbileValue)
	else:
		templist=allPossbileValue
	dictToSave={}
	logging.basicConfig(format='%(asctime)s %(message)s',filename='test.log',level=logging.DEBUG)
	logging.info('序列检测开始....')
	for i in range(len(lisToCheck)/2):
		
		for key,value in enumerate(templist):
			
			
			if (lisToCheck[2*i],lisToCheck[2*i+1])==value:
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

	fj=open('data2.dat','r')
	for eachline in fj:
		a1= [int(x) for x in eachline.strip('\n').strip(' ').split(' ')]
		s1.extend(a1)
	fj.close()

	
	
	logging.info('sequence to be tested is :%s' % str(s1))

	tuple1=((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), 
		(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), 
		(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), 
		(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), 
		(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), 
		(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6))

	t=comp_sequence(s1,tuple1)

	

	for value in t.values():
		list2.append([1.0/36,value])
		


	f=com_kfang(list2,len(s1)/2)
	print f


