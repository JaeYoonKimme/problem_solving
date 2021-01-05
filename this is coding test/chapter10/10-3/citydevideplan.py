n,m=map(int,input().split())
edge=[]
parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b



result=[]
for i in range(m):
    a,b,cost=map(int,input().split())
    edge.append((cost,a,b))
edge.sort()
for i in edge:
    if find_parent(parent,i[1])==find_parent(parent,i[2]):
        continue
    
    else:
        union_parent(parent,i[1],i[2])
        result.append(i[0])

result.sort()

print(sum(result)-max(result))


