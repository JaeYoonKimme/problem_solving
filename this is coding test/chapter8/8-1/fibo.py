def fibo(n):
    if n==1 or n==2:
        return 1
    
    return fibo(n-1)+fibo(n-2)


print(fibo(100)) #컴퓨터로 연산이 불가능