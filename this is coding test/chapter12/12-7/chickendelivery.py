n,m=map(int,input().split())
city=[]
for i in range(n):
    city.append(list(map(int,input().split())))

house=[]
chicken=[]

for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            house.append([9999,i,j])
        elif city[i][j]==2:
            chicken.append([0,i,j])

for i in house:
    for j in chicken:
        j[0]+=(abs(i[1]-j[1])+abs(i[2]-j[2]))



chicken=sorted(chicken)
answer=0

for i in house:
    for j in range(m):
        i[0]=min(i[0], (abs(i[1]-chicken[j][1])+abs(i[2]-chicken[j][2])) )
    answer+=i[0]


print(answer)



