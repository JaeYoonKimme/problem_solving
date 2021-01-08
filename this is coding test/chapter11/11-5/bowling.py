n,m=map(int,input().split())
ball=list(map(int,input().split()))

result=0
for i in range(n):
    for j in range(i+1,n):
        if ball[i]!=ball[j]:
            result=result+1

print(result)