s=str(input())

result=0
for i in s:
    cost=int(i)
    result=max(result*cost,result+cost)

print(result)