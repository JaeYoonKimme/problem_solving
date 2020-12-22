N=int(input())
market=list(map(int,input().split()))

M=int(input())
order=list(map(int,input().split()))

array=[0]*1000000

for i in market:
    array[i]=1

for j in order:
    if array[j]==1 :
        print("yes")
    
    else :
        print("no")