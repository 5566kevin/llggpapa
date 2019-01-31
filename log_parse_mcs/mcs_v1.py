f=open('./log_5min.txt', 'r')

tmp=[]

cqi4=[]
mcs1=[]
mcs2=[]

match=0

value=''
strg=''

'''
detect sinr first and mcs next
'''

for line in f:
    tmp=line.strip().split(' ')
    try:
        if match==0 and tmp[7]=='SINR:' and tmp[12][0]=='4':    
            #cqi4.append(tmp[10][2])
            strg=strg+str(int(tmp[10][2],16))
            strg=strg+','
            match=1
        elif match==1 and tmp[19]=='MCS1':
            value=tmp[21].strip().split(',')[0]
            strg=strg+value
            strg=strg+','
            value=tmp[30].strip().split(',')[0]
            strg=strg+value
            print strg
            strg=''
            match=0
            #mcs1.append(tmp[21].strip().split(',')[0])
            #mcs2.append(tmp[30].strip().split(',')[0])
    except:
        continue
