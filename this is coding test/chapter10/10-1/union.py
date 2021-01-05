'''
def find_root(parent,x):
    if parent[x]!=x:
        return find_root(parent,parent[x])
    return x
'''
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

for i in range(e):
    a,b=map(int,input().split())
    make_union(parent,a,b)

for i in range(1,v+1):
    print(find_root(parent,i),end=' ')

print()

for i in range(1,v+1):
    print(parent[i],end=' ')