s=str(input())


result=[0]*2
n=len(s)

for i in range(n):
    now=int(s[i])

    if i==0:
        result[now]=result[now]+1
    
    elif int(s[i-1])!=now:
        result[now]=result[now]+1

    else:
        continue

print(min(result[0],result[1]))
print(result)