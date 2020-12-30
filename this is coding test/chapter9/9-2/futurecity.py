import heapq

n,m=map(int,input().split()) #n=회사의 갯수 m=경로의 갯수
INF=int(1e9)

distance=[INF]*(n+1)


graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

x,k=map(int,input().split())

def dijkstra(start) :
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for j in graph[now]:
            cost=dist+j[1]
            if cost<distance[j[0]]:
                distance[j[0]]=cost
                heapq.heappush(q,(cost,j[0]))


result=0

dijkstra(1)
result=result+distance[k]

dijkstra(k)
result=result+distance[x]


print(result)