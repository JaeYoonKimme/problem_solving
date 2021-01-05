v,e=map(int,input().split())

parent=[0]*(v+1)
for i in range(1,v+1):
    parent[i]=i
edge=[]

for i in range(e):
    a,b,c=map(int,input().split())
    edge.append((c,a,b))

edge=sorted(edge)

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

result=0
for el in edge:
    if find_parent(parent,el[1])==find_parent(parent,el[2]):
        continue
    
    else:
        union_parent(parent,el[1],el[2])
        result=result+el[0]

print(result)