f=open('./0717.txt', 'r')

tmp=[]
cqi=[]
mcs=[]
mcs2=[]

for line in f:
	tmp=line.strip().split(' ')
	try:
		if tmp[3]!='enb2':
			continue
		if tmp[7]=='SINR:' and tmp[12][0]=='4':
			cqi.append(int(tmp[10][2],16))
			mcs.append(0)
			mcs2.append(0)
		if tmp[19]=='MCS1':
			mcs.append(int(tmp[21].strip().split(',')[0]))
			mcs2.append(int(tmp[30].strip().split(',')[0]))
			cqi.append(0)
	except:
		continue

tmp=''
for i in range(len(mcs)):
	tmp=tmp+str(cqi[i])
	tmp=tmp+','
	tmp=tmp+str(mcs[i])
	tmp=tmp+','
	tmp=tmp+str(mcs2[i])
	print tmp
	tmp=''

