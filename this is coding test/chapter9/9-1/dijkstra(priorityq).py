import heapq
import sys
input=sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

start= int(input())

graph=[[] for i in range(n+1)]

#visited=[False]*(n+1)

distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))


def dijkstra(start):
    q=[]
    #시작노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0,start)) #거리, 노드 인덱스 순서
    distance[start]=0
    #큐가 비어있지 않다면 while
    while(q):
        #가장 최단 거리가 짧은 노드에 대해서 정보 꺼내기
        plus,idx=heapq.heappop(q)

        # 이미 처리된 적이 있다면 무시
        if distance[idx]<plus:
            continue


        #현재 노드와 연결된 다른 노드를 확인
        for i in graph[idx]:
            #현재 노드를 걸쳐서 다른 노드에 가는 거리가 짧은 경우
            cost=i[1]+plus
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))



dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")

    else :
        print(distance[i])
