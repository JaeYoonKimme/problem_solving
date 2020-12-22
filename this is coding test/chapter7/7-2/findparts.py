#이진탐색을 이용한 풀이

def binarysearch(array,target,start,end):
    if start>end:
        return -1

    middle=(start+end)//2

    if array[middle]==target:
        return middle

    elif array[middle]>target:
        return binarysearch(array,target,start,end-1)
    
    else :
        return binarysearch(array,target,start+1,end)



N=int(input())
market=list(map(int,input().split()))

M=int(input())
order=list(map(int,input().split()))


for i in order:
    if (binarysearch(market,i,0,N-1)>-1):
        print("yes")
    else:
        print("no")

