v,e=map(int,input().split())

graph=[[] for i in range(v+1)]
visited=[False]*(v+1)

for i in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)

result=[]
def dfs(graph,v,visited):
    visited[v]=True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    result.append(v)

dfs(graph,1,visited)
for i in result:
    print(i,end=' ')


