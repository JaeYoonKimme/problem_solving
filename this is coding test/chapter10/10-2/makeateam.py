n,m=map(int,input().split())

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

for i in range(m):
    n,a,b=map(int,input().split())
    if n==0:
        union_parent(parent,a,b)
        

    elif n==1:
        c=find_parent(parent,a)
        d=find_parent(parent,b)
        if c==d:
            print("YES")
        else :
            print("NO")