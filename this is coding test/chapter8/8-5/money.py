n,m=map(int,input().split())

money=[]
for i in range(n):
    money.append(int(input()))

d=[10001]*(m+1)
d[0]=0
#print(d)

for k in money:
    for j in range(k,m+1):
        if j-k>=0:
            d[j]=min(d[j-k]+1,d[j])
    #print(d)

if d[m]==10001:
    print(-1)

else:
    print(d[m])