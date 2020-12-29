import sys
input=sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

start= int(input())

graph=[[] for i in range(n+1)]

visited=[False]*(n+1)

distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def getsmalldistance():
    min_val=INF
    idx=0
    for i in range(1,n+1):
        if distance[i]<min_val and visited[i]==False:
            min_val=distance[i]
            idx=i
    return idx

def dijkstra(start):
    #시작노드 에 대해서 초기화
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]

    #시작 노드를 제외한 n-1개의 노드에 대해서 초기화
    for i in range(1,n-1): #인덱스와 상관없는 단순 반복횟수값

        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now=getsmalldistance()
        visited[now]=True

        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost=j[1]+distance[now]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[j[0]]:
                distance[j[0]]=cost


dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")

    else :
        print(distance[i])
    
    
