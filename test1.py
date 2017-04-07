import random

list1=[]

fj=open('test.txt','w')


for i in range(360):
	list1.append(random.randrange(1,7))


fj.write(str(list1)+'\n')

tuple1=((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), 
	(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), 
	(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), 
	(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), 
	(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), 
	(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6))


def comp(lis):
	dict1={}
	
	for i in range(len(lis)/2):
		
		for key,value in enumerate(list(tuple1)):
			
			
			if (lis[2*i],lis[2*i+1])==value:
				if key in dict1:
					dict1[key]+=1
				else:
					dict1[key]=1
				break

	return dict1


t=comp(list1)

for key,value in t.items():
	#print str(tuple1[key]) +'='+str(value)
	fj.write(str(tuple1[key]) +'='+str(value)+'\n')


fj.close()

