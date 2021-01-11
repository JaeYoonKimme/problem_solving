def solution(key, lock):
    answer = True
    n=len(lock)
    m=len(key)
    
    new_lock=[[0]*(n*3) for i in range(n*3)]
    
    for i in range(n):
        for j in range(n):
                new_lock[i+n][j+n]=lock[i][j]

    
    for _ in range(4):
        key=rotate(key)
        
        for x in range(n*2):
            for y in range(n*2):
                
                for i in range(m):
                    for j in range(m):
                        new_lock[i+x][j+y]+=key[i][j]
                
                if check(new_lock)==True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[i+x][j+y]-=key[i][j]

    return False

def check(new_lock):
    l=len(new_lock)//3
    for i in range(l,l*2):
        for j in range(l,l*2):
            if new_lock[i][j]!=1:
                return False
    return True


def rotate(key):
    n=len(key)
    m=len(key[0])
    result=[[0]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
                result[j][n-1-i]=key[i][j]
    
    return result

    


key=[
    [0,0,0],
    [1,0,0],
    [0,1,1]
]
lock=[
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
print(solution(key,lock))