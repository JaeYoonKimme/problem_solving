def spreadVirus(x,y,tube,visited):
    vType=tube[x][y]
    
    if x-1>-1:
        if tube[x-1][y]==0:
            tube[x-1][y]=vType
    
    if x+1<n:
        if tube[x+1][y]==0:
            tube[x+1][y]=vType

    if y-1>-1:
        if tube[x][y-1]==0:
            tube[x][y-1]=vType
    
    if y+1<n:
        if tube[x][y+1]==0:
            tube[x][y+1]=vType

    visited[x][y]=True


n,k=map(int,input().split())

tube=[]

for i in range(n):
    tube.append(list(map(int,input().split())))

s, x, y=map(int,input().split())

visited=[[False]*(n) for i in range(n)]



for time in range(s):
    virus=[]
    for i in range(n):
        for j in range(n):
            if tube[i][j]!=0 and visited[i][j]==False:
                virus.append((tube[i][j],(i,j)))

    virus=sorted(virus)
    for v in virus:
        spreadVirus(v[1][0],v[1][1],tube,visited)


print(tube[x-1][y-1])

#time over 로 실패했다 아이디어 새로 짜서 다시 도전할 것 




