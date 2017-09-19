import logging
import win32com.client
import time

'''
def random_range(min_bound, max_bound):
    interval_len = max_bound - min_bound + 1
    qng = win32com.client.Dispatch("QWQNG.QNG")
    rand32 = qng.RandInt32
    return min_bound + rand32 % interval_len

k=1

logging.basicConfig(format='%(asctime)s %(message)s',filename='aaalog.txt',level=logging.INFO)
fj=open('aaa.txt','w+')

s1=time.time()

while time.time()-s1<3600:
    if k%3:
        randnumber=random_range(1,6)
        fj.write(str(randnumber)+' ')
        logging.info('%d has produce' %randnumber)
        k+=1
    else:
        randnumber = random_range(1, 6)

        fj.write(str(randnumber)+'\n')
        logging.info('%d has produce' %randnumber)
        k=1

fj.close()
'''
class randomEvent():
    def __init__(self,name):
        self.name=name
    def generNumber(self,min_bound=1,max_bound=6):
        interval_len = max_bound - min_bound + 1
        qng = win32com.client.Dispatch(self.name)
        rand32 = qng.RandInt32
        return min_bound + rand32 % interval_len

re=randomEvent('QWQNG.QNG')
for i in range(3):
    rng=re.generNumber(10,20)
    print rng