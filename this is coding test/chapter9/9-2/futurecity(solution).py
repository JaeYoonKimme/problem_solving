import heapq

n,m=map(int,input().split()) #n=회사의 갯수 m=경로의 갯수
INF=int(1e9)

graph=[[INF]*(n+1) for _ in range(n+1)]


for i in range(1,n+1):
    graph[i][i]=0

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k=map(int,input().split())

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])

print(graph[1][k]+graph[k][x])