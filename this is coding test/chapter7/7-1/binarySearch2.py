def binarySearch(array,target,start,end):
    
    while start<=end:
        middle=(start+end)//2

        if array[middle]==target:
            return middle
        
        elif array[middle]>target:
            end=middle-1
        
        elif array[middle]<target:
            start=middle+1

    return None



array=[1,2,3,4,6,6,7,8,9,10]

print(binarySearch(array,10,0,9))