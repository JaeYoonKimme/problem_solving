n=int(input())
result=[]
for i in range(n):
    result.append(input().split())

result= sorted(result, key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]) )

for i in range(n):
    print(result[i][0])
