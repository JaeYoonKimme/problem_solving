def open(A,isopened,x,y,pre_x,pre_y):
    if x<0 or x>n-1 or y<0 or y>n-1:
        return
    
    elif isopened[x][y]==True:
        return
        open(A,isopened,x+1,y,x,y)
        open(A,isopened,x-1,y,x,y)
        open(A,isopened,x,y+1,x,y)
        open(A,isopened,y-1,x,y)
    
    elif abs(A[pre_x][pre_y]-A[x][y])>=n and abs(A[pre_x][pre_y]-A[x][y])<=r:
        #count+=1
        isopened[x][y]=True
        average=(A[pre_x][pre_y]+A[x][y])//2
        A[x][y]=average
        A[pre_x][pre_y]=average
        print("reached here!")
        open(A,isopened,x+1,y,x,y)
        open(A,isopened,x-1,y,x,y)
        open(A,isopened,x,y+1,x,y)
        open(A,isopened,x,y-1,x,y)


n,l,r=map(int,input().split())
A=[]
for i in range(n):
    A.append(list(map(int,input().split())))

isopened=[ [False]*n for i in range(n)]
count=0


open(A,isopened,1,0,0,0)
open(A,isopened,0,1,0,0)

print(count)



    
    
    
