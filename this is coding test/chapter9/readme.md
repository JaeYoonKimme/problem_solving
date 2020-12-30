# 9. 최단 경로

* 최단경로 알고리즘은 말 그대로 가장 짧은 거리를 찾는 알고리즘을 의미한다  
특정 지점에서 특정 지점까지의 거리를 찾는 경우도 있고, 특정 지점에서 모든 지점까지의 거리를 구하는 경우도 있다.  

## 다익스트라 최단경로 알고리즘  
다익스트라 최단경로 알고리즘은 최단경로 알고리즘중 하나로 다음과 같이 동작하며 출발 노드에서 각각의 노드까지의 최단경로를 구해준다  
1. 출발 노드를 정한다  
2. 인접 노드 테이블을 초기화한다(출발노드에서 각각의 노드까지의 거리를 저장하는 1차원 배열)  
3. 방문하지 않은 노드 중 리스트에서 가장 거리가 짧은 노드를 선택한다   
4. 인접한 노드까지의 테이블의 거리정보를 업데이트하고, 선택한 노드를 방문 처리한다 (3,4반복)


  
  3번에서 거리정보는 항상 업데이트 하는 것이 아니라 저장된 정보보다 짧은 값이 나타나는 경우에 업데이트 한다.  
### 1. 간단한 구현의 다익스트라 알고리즘  
  책에서는 두가지 버젼으로 다익스트라 알고리즘을 구현했다 먼저 간단하지만 시간복잡도가 높은 구현법이다.  
  처음엔 코드를 읽으며 이해하였고, 주석만 먼저 입력한 후 스스로 구현해보려고 했다.  
```python
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
    
    
```

### 2. 개선된 다익스트라 알고리즘
위의 알고리즘은 getsmalldistance()함수 호출시 매번 최단거리 테이블을 선형탐색하면서 시간이 걸린다.
하지만 힙(Heap)자료구조를 이용해서 더욱 빠르게 탐색을 수행하면서 탐색시간을 줄일 수 있다.   
* 다익스트라 알고리즘의 빠른 탐색을 위해서는 우선순위 큐 라는 자료구조를 이용할 수 있다.
우선순위 큐는 힙 구조를 통해서 구현하는데 이를 위해서 먼저 힙에 대해서 공부해 보았다.   

#### (힙 구조)  
힙 자료구조는 완전이진트리의 형태로 되어있는 자료구조이다(완전 이진 트리는 부모노드당 자식노드가 두개씩 왼쪽부터 채워지는 구조)  
이때 부모노드의 우선순위는 자식노드의 우선순위보다 항상 크다!  
간단한 기능구현만 설명해보면  
삽입 : 가장 끝에 노드를 삽입하고, 부모노드와 비교하며 교체한다  
삭제 : 루트노드를 꺼내고, 가장 끝의 노드를 루트자리에 넣는다. 그후 자식노드와 비교하며 우선순위가 둘중 큰것을 올린다

#### (우선순위 큐)
우선순위 큐는 큐와같이 삽입과 삭제 기능을 지원하고, 삭제의 기준이 우선순위(정렬기준)에 따르는 자료구조이다.  
따라서 값을 저장할때 힙 구조를 사용한다.  
파이썬에서는 최소힙 구조를 지원하므로 다익스트라 최단경로 알고리즘에서는 그대로 사용이 가능하다.
 

```python
#개선된 다익스트라 최단거리 알고리즘

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
```

## 플로이드 워셜 알고리즘  
플로이드 워셜 알고리즘은 2차원 리스트를 사용하여 거리정보를 갱신하는 방식의 알고리즘이다.  
다익스트라 알고리즘과 달리 특정 시작노드가 아니라 모든 지점에서 모든 지점으로 가는 거리정보를 파악한다.  
N개의 노드에 대해서 수행하고, 매번 N^2의 이차원 리스트를 갱신하므로 시간복잡도는 O(N^3)이다.  
간단하게 알고리즘을 설명해보면 다음과 같다.
- n개의 노드를 하나씩 선택하며 진행한다.
- 선택한 노드를 거쳐가는 모든 경로를 탐색하고, 거쳐가는 길이 더 짧으면 리스트를 갱신한다.
- Dab=a에서 b까지의 거리라고 할 때 다음과같이 점화식을 쓸 수 있다. 
- Dab=min(Dab,Dak,Dkb)

```python
#플로이드 워셜 알고리즘 구현 
NF = int(1e9)

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
#여기까지 진행하면 리스트에 모든 거리정보가 업데이트된다
```



