import heapq
INF=int(1e9)
n,m,c=map(int,input().split())

graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for i in range(m):
    a,b,d=map(int,input().split()) #앞에서 C라는 변수를 사용했으니까 안겹치게 신경써야해 
    graph[a].append((b,d))

def dijkstra(start): #start에 c를 넣는다
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        
        for j in graph[now]:
            cost=dist+j[1]
            if cost<distance[j[0]]:
                distance[j[0]]=cost
                heapq.heappush(q,(cost,j[0]))

dijkstra(c)

lst=[]
count=0
for i in range(1,n+1):
    if distance[i]!=INF and distance[i]!=0:
        count=count+1
        lst.append(distance[i]) #비교를 해야할때는 max를 써도 좋음 result=max(result,distance[i])
    #print(distance[i])

print(count,"",max(lst))
