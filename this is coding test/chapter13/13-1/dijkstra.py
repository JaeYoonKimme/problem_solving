import heapq

INF = int(1e9)

n,m,k,x=map(int,input().split())

graph=[[] for _ in range(n+1)]

distance=[INF]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))

def dijkstra(x):
    q=[]
    heapq.heappush(q, (0,x))
    distance[x]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost=i[1]+dist

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost,i[0]))


dijkstra(x)

result=-1
#print(distance)
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        result+=1

if result==-1:
    print(result)