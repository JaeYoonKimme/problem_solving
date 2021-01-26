from collections import deque
from itertools import combinations
import copy

def dfs(nlab,x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if nlab[x][y]==0:
        nlab[x][y]=2
        

        dfs(nlab,x-1,y)
        dfs(nlab,x,y-1)
        dfs(nlab,x+1,y)
        dfs(nlab,x,y+1)
        return True
    #print(nlab)
    return False 

n,m=map(int,input().split())

lab=[]
for i in range(n):
    lab.append(list(map(int,input().split())))


#바이러스의 위치 따로 저장
#0인 부분을 따로 저장
notwall=[]
virus=[]
for i in range(n):
    for j in range(m):
        if lab[i][j]==0:
            notwall.append((i,j))
        elif lab[i][j]==2:
            virus.append((i,j))

#벽이 아닌 부분중에서 3개를 뽑기
newwall=list(combinations(notwall,3))
result=0
for combi in newwall:
    nlab=copy.deepcopy(lab)
    count=0
    for i in combi:
        nlab[i[0]][i[1]]=1
    for j in virus:
        dfs(nlab,j[0]-1,j[1])
        dfs(nlab,j[0],j[1]-1)
        dfs(nlab,j[0]+1,j[1])
        dfs(nlab,j[0],j[1]+1)

    for i in range(n):
        for j in range(m):
            if nlab[i][j]==0:
                count+=1
    
    result=max(result,count)


print(result)





    

    
        
    
    
