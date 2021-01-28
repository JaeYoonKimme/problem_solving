from collections import deque

n,k=map(int,input().split())
tube=[]
for i in range(n):
    tube.append(list(map(int,input().split())))

s, target_x, target_y=map(int,input().split())

virus=[]
for i in range(n):
    for j in range(n):
        if tube[i][j]!=0:
            virus.append((tube[i][j],0,i,j))

virus.sort()
q=deque(virus)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

while q:
    v,time,x,y=q.popleft()
    
    if time==s:
        break

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>-1 and nx<n and ny>-1 and ny<n:
            if tube[nx][ny]==0:
                tube[nx][ny]=v
                q.append((v,time+1,nx,ny))

print(tube[target_x-1][target_y-1])
 





