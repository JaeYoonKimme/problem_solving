n, k =map(int,input().split())

arrayA=[]
arrayB=[]

arrayA=list(map(int,input().split()))
arrayB=list(map(int,input().split()))

for i in range(k):
    arrayA=sorted(arrayA)
    arrayB=sorted(arrayB, reverse=True)

    arrayA[0], arrayB[0] = arrayB[0], arrayA[0]

sum=0
for el in arrayA:
    sum=sum+el

print(sum)