from collections import deque

def bfs(graph,v,visited):

    queue=deque([v])
    visited[v]=True
    
    while queue:
        now=queue.popleft()
        print(now,end=' ')

        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True





graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited=[False]*9

bfs(graph,1,visited)