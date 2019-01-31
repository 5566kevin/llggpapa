import numpy as np
from collections import Counter

f=open('./syslog', 'r')
tmp=[]

cnt=0

cqi1=[]
cqi4=[]
time=[]

for line in f:
	tmp=line.strip().split(' ')
	if tmp[2]!=time:
		print time
		print Counter(cqi1).most_common()
		print Counter(cqi4).most_common()
		cqi1=[]
		cqi4=[]
		time=tmp[2]
		continue
	try:	
		if tmp[7]=='SINR:':
			if tmp[12][0]=='1':
				cqi1.append(tmp[10][2])
			elif tmp[12][0]=='4':
				cqi4.append(tmp[10][2])
	except:
		continue
