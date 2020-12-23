n,m=map(int,input().split())

ricecake=list(map(int,input().split()))

sum=0
i=0
while True:
    sum=0
    i=i+1

    for el in ricecake:
        s=el-i
        if s<0:
            s=0
        sum=sum+s
    if (sum==m):
        break

print(i)