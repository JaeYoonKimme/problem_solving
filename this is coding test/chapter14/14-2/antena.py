n = int(input())


house=list(map(int,input().split()))
house.sort()

i=n//2

if (n%2==1):
    print(house[i])
else:
    print(house[i1])

if n % 2 == 1:
    print(house[len(house) // 2])
else:
    print(house[len(house) // 2 - 1])

