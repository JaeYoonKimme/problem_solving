# 그래프 이론
## 1.서로소 집합  
집합은 원소들의 나열이라고 할 수 있다. 이때 두 집합이 공통된 원소를 포함하지 않는 경우,  
즉 공통된 원소가 없는 두 집합을 서로소 관계라고 한다.  
서로소 집합 자료구조는 union,find 두개의 함수로 구현하고 기능한다.  
* union : 두 원소의 부모노드를 같게한다(일반적으로 더 작은쪽을 따라감)  
* find  : 원소의 최종 부모노드를 찾아 반환

먼저 find함수를 구현해보았다.
```python
def find_root(parent,x):
    if parent[x]!=x:
        return find_root(parent,parent[x])
    return x
```
위의 코드는 재귀적으로 find함수를 호출하며 루트노드를 반환한다  
이를 경로압축기법으로 최적화하면 그때그때 부모노드의 값을 갱신하면서 호출되는 빈도를 최소화할수있다.
```python
def find_root(parent,x):
    if parent[x]!=x:
        parent[x]=find_root(parent,parent[x])
    return parent[x]
```
Union함수 구현
```python
def union_parent(parent,a,b):
    a=find_root(parent,a)
    b=find_root(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b
```

서로소 집합 자료구조를 활용하면 무방향 그래프 내에서 사이클 유무 판별이 가능하다.
```python
Cycle=False
for i in range(e):
    a,b=map(int,input().split())
    if find_root(parent,a)==find_root(parent,b):
        Cycle=True
        
    else:
        make_union(parent,a,b)
```
입력되는 정보를 하나씩 판별하며 두 원소의 부모노드가 다를때만 유니온을 한다.  
그러다 두 원소의 부모가 같은 경우가 나올 경우 싸이클이 일어난 것을 확인할 수 있다.  
근데 만약에 사이클의 갯수를 확인하고싶으면 어떻게 해야할까??

## 2.신장트리  
모든 원소가 연결되어있으면서 사이클이 일어나지 않는 부분 그래프를 신장트리라고 한다.(트리의 조건이기도 함)
그래프 내에서 최소 신장트리를 찾아야 하는 경우가 있다(모든 도시를 연결해야하는데 최소로 다리를 놓는 경우)  
이를 최소신장 트리 알고리즘이라고 하는데, 대표적으로 크루스칼 알고리즘이 있다.

### *크루스칼 알고리즘  
먼저 간선의 정보를 정렬한다. 거리가 짧은 간선부터 집합에 포함시키는데, 사이클을 발생시키는 경우 포함시키지 않는다.  
1. 간선 데이터를 오름차순 정렬한다.  
2. 간선을 하나씩 확인하며 현재 간선이 사이클을 만들지 않는지 확인한다.  
-사이클을 안 만들 경우 최소 신장트리에 포함시킨다.  
-사이클을 만들 경우 포함시키지 않는다.  

크루스칼 알고리즘은 간선정보를 정렬하고, 작은것부터 하나씩 확인하며 서로소 자료구조 연산을 수행하면 된다.
```python
#여기서 edge 리스트는 (비용,노드a,노드b)인 튜플로 구성되어있고, 비용으로 정렬되어있다.
result=0
for el in edge:
    if find_parent(parent,el[1])==find_parent(parent,el[2]):
        continue
    
    else:
        union_parent(parent,el[1],el[2])
        result=result+el[0]

print(result)
```

## 3.위상정렬  
위상정렬은 정렬 알고리즘의 일종으로 방향그래프의 모든 노드를 방향성에 거스르지 않게 정렬하는 것이다.  

그래프에서 한 노드로 들어오는 간선의 갯수를 진입차수라고 한다.(indegree) 

진입차수를 이용한 위상정렬의 알고리즘은 다음과 같다.
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐에서 노드를 꺼내고, 해당 노드에 연결된 간선을 제거한다.
3. 진입차수가 0이 된 노드를 큐에 넣는다.(2로가서 반복)

이때 모든 원소를 방문하기 전에 큐가 비는경우, 사이클이 발생한 것이다.  

```python
def topology_sort():
    q=deque()
    result=[]
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now=q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]=indegree[i]-1 #간선을 제거하는 코드는 진입차수만 줄여주면 된다. 그래프 초기정보는 건들지 않음 
            if indegree[i]==0:
                q.append(i)
    
    for i in result:
        print(i,end=' ')
```

외에도 DFS를 이용하면 위상정렬을 구할수있다고한다.(단 사이클이 없다는 가정)
```python
result=[]
def dfs(graph,v,visited):
    visited[v]=True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    result.append(v)

dfs(graph,1,visited)
for i in result:
    print(i,end=' ') #역순으로 출력된다
```