def binarySearch(array,target,start,end):
    if start>end:
        return None
    middle=(start+end)//2
   

    if array[middle]==target:
        return middle

    elif array[middle]>target:
        return binarySearch(array,target,start,middle-1)
    
    else :
        return binarySearch(array,target,middle+1,end)


array=[1,2,3,4,6,6,7,8,9,10]

print(binarySearch(array,4,0,9))