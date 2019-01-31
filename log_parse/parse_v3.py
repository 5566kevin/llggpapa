from collections import Counter

f=open('./log_5min.txt', 'r')

tmp=[]
tmp2=[]

cqi4=[]
time=[]

datalist=[]     #(time, most CQI, times of CQI)

#{'f': 32, 'd': 7, 'c': 2, 'e': 2, 'b': 1}

acc=0
weight=0

for line in f:
    tmp=line.strip().split(' ')
    if tmp[2]!=time:
        #print time
        if len(cqi4)!=0:
            acc=0
            weight=0
            #print time
            for i in range(len(Counter(cqi4))):
                tmp2=Counter(cqi4).most_common()[i]
                acc=acc+int(tmp2[0],16)*tmp2[1]
                weight=weight+tmp2[1]
            datalist.append(acc/float(weight))
            #tmp2=Counter(cqi4).most_common(1)[0]
            #datalist.append((time,int(tmp2[0],16),tmp2[1]))
        cqi4=[]
        time=tmp[2]
        continue
    try:
        if tmp[7]=='SINR:' and tmp[12][0]=='4':
            cqi4.append(tmp[10][2])
    except:
        continue


for i in range(len(datalist)):
    #print i,
    #print '\t',
    print datalist[i]

