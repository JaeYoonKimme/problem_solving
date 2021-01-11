n=int(input())
k=int(input())
data=[ [0]*(n+1) for _ in range(n+1)]
turn=[]

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b]=1


l=int(input())
for _ in range(l):
    a,b=(input().split())
    turn.append((int(a),b))
turn.sort()


headx=1
heady=1


time=0
head_history=[]
dirx=[1,0,-1,0]
diry=[0,1,0,-1]
dir_index=0
while True:
    time+=1
    
    
        
    data[headx][heady]=2 #tail
    head_history.append((headx,heady))

        #move
    headx+=dirx[dir_index]
    heady+=diry[dir_index]
        
        #cheack if snake meets wall or tail
    if headx>n or headx<1 or heady>n or heady<1:
        print(time)
        #print("snake met wall")
        break

    elif data[headx][heady]==2:
        print(time)
        #print("snake met tail")
        break
        
    #check if snake ate apple
    if data[headx][heady]==1:
        data[headx][heady]=0
    
    else:
        a,b=head_history[0]
        data[a][b]=0
        head_history.remove(head_history[0])
    

    #switch direction
    if len(turn)!=0 and (turn[0][0]==time):
        if turn[0][1]=="D":
            dir_index+=1
            dir_index%=4
        else:
            dir_index-=1
            dir_index%=4
        turn.remove(turn[0])

#꼬리부분에 대한 처리가 제대로 이루어지지 않고있음 


    
        
    
