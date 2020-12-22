def sequentialSearch(n, target, array):
    for i in range(n):
        if array[i]==target:
            return(i+1)
    #n개의 원소에 대해서 n번만큼의 연산이 필요함 O(n)

array=["pizza","hamburger","spaghetti", "gimbap"]

print(sequentialSearch(len(array),"pizza",array))

