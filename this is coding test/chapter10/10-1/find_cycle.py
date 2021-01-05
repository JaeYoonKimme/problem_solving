def find_root(parent,x): #경로압축기법 적용 
    if parent[x]!=x:
        parent[x]=find_root(parent,parent[x])
    return parent[x]

def make_union(parent,a,b):
    a=find_root(parent,a)
    b=find_root(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i
Cycle=False
for i in range(e):
    a,b=map(int,input().split())
    if find_root(parent,a)==find_root(parent,b):
        Cycle=True
        
    else:
        make_union(parent,a,b)

if (Cycle):
    print("Cycle has occured")
else:
    print("There is no cycle")