n,m,k= map(int,input().split())

l=list(map(int,input().split()))

l.sort()
first=l[n-1]
second=l[n-2]
result=0
count=0
for i in range(m):
    if count==k:
        result=result+second
        count=0
        continue
    result=result+first
    count=count+1

print(result)
