from itertools import combinations

n,m=map(int,input().split())
city=[]
for i in range(n):
    city.append(list(map(int,input().split())))

house=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            house.append([i,j])
        elif city[i][j]==2:
            chicken.append([i,j])

chicken=list(combinations(chicken,m))
result=99999
for com in chicken:
    total=0
    for h in house:
        distance=99999
        for chick in com:
            distance=min(distance,abs(chick[0]-h[0])+abs(chick[1]-h[1]))
        total=total+distance
    result=min(result,total)

print(result)


