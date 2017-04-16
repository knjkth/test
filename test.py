from time import ctime

fj = open('number.txt','r')

a=5
count=0
print ''
try:
	for i in fj:
		p=[int(x) for x in str(i).strip('\n').strip().split(' ')]
		count+=p.count(a)

except StopIteration:
	print 'error'
	

print count
fj.close()






