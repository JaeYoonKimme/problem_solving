n,m=map(int,input().split())
ball=[0]*11

data=list(map(int,input().split()))

for x in data:
    ball[x]=ball[x]+1
result=0
for i in range(1,m+1):
    n=n-ball[i]
    result=result+(n*ball[i])

print(result)