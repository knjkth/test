

t=[87,77,92,68,80,78,84,77,81,80,80,77,92,86,76,80,
81,75,77,72,81,72,84,86,80,68,77,87,76,77,78,92,75,80,78]

s=sorted(t)

print s



sum=0

for i in range(len(s)):
	sum+=s[i]

miu=float(sum)/len(s)


sum=0

for i in range(len(s)):
	sum+=(s[i]-miu)**2

sig=pow(sum/len(s),0.5)




print miu
print sig

