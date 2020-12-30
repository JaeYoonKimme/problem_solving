INF = int(1e9)

n=int(input())
m=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i]=0

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])

#outputpart
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print("INF",end=" ")
        else:
            print(graph[i][j],end=" ")
    print("")
    