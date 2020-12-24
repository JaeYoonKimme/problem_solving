import sys

n=int(input())
d= [0]*30001
sys.setrecursionlimit(10000) 

def makeitone(x):
    if x<1:
        return 1000
    if x==2:
        return 1

    if d[x-1]!=0:
        d[x]=d[x-1]+1
    else : 
        d[x]=makeitone(x-1)+1
    
    if x%5 ==0:
        if d[x//5]!=0:
            d[x]=min(d[x],d[x//5]+1)
        else :
            d[x]=min(d[x],makeitone(x//5)+1)

    if x%3 ==0:
        if d[x//3]!=0:
            d[x]=min(d[x],d[x//3]+1)
        else :
            d[x]=min(d[x],makeitone(x//3)+1)
    
    if x%2 ==0:
        if d[x//2]!=0:
            d[x]=min(d[x],d[x//2]+1)
        else :
            d[x]=min(d[x],makeitone(x//2)+1)
    
    return d[x]

print(makeitone(n))

#2500정도가 넘어가면 역시 뭔가 문제가 생기는지 값 반환 없이 프로그래밍이 끝난다
#반복문을 활용해서 바텀업 방식으로 다이나믹 프로그래밍을 하는것이 좋아보인다.