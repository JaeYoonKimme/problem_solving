import sys
import heapq
input=sys.stdin.readline
INF = int(1e9)

n,m= map(int,input().split())

start=int(input())

visited=[False]*(n+1)

graph=[[] for _ in range (n+1)]

distance=[INF]*(n+1)



for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q :
        dist,now=heapq.heappop(q)
        
        if distance[now]<dist:
            continue

        for j in graph[now]:
            cost=dist+j[1]
            if cost<distance[j[0]]:
                distance[j[0]]=cost
                heapq.heappush(q,(cost,j[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])