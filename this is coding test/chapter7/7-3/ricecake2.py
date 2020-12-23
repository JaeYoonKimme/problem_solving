n,m=map(int,input().split())

ricecake=list(map(int,input().split()))


start=0
end=max(ricecake)
result=0

while start<=end:
    middle=(start+end)//2
    sum=0
    for el in ricecake:
        if el>middle:
            sum=sum+(el-middle)

#    if sum==m:
#        print(middle)
#        break
    
    if sum<m:
        end=middle-1
    
    else :
        result=middle
        start=middle+1

print(result)