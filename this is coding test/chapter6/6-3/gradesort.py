n=int(input())

array=[]

for i in range(n):
    data=input().split()
    array.append((data[0],int(data[1])))

array=sorted(array, key=lambda x : x[1]) #특정 key값으로 정렬하는 방법 

for el in array:
    print(el[0], end=" ")