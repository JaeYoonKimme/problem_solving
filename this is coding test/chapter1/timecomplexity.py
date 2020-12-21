from random import randint
import time

array1 = []
array2 = []

for _ in range(10000):
    array1.append(randint(1,100))
    array2.append(randint(1,100))

start_time=time.time()


for i in range(len(array1)):
    min_idx=i
    for j in range(i+1,len(array1)):
        if array1[min_idx]>array1[j]:
            min_idx=j
    array1[i], array1[min_idx] = array1[min_idx], array1[i] #swap

end_time=time.time()
print("selectionsort :",end_time-start_time)

start_time=time.time()
array2.sort()
end_time=time.time()
print("python library :",end_time-start_time)





