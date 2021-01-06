n=int(input())

frate=list(map(int,input().split()))

frate=sorted(frate)


count=0
result=0
for i in frate:
    count=count+1

    if count>=i:
        result=result+1
        count=0
     
print(result)
 
        