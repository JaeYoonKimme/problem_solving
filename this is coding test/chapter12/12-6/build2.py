def solution(n, build_frame):
    town=[[[]for _ in range(n+1)] for _ in range(n+1)]
    
    #start
    for el in build_frame:
        x=el[0] #x좌표
        y=el[1] #y좌표
        a=el[2] #건물의 종류 0->기둥 1->보
        b=el[3] #설치혹은철거 0->철거 1->설치

        past_town=town

        if b==0:
            town[y][x].remove(a)

        else :
            town[y][x].append(a)

        back=False
        for i in range(n+1):
            for j in range(n+1):
                if check(i,j,town,n)==False:
                    back=True
        
                    

        if back==True:
            if b==0:
                town[y][x].append(a)
            else:
                town[y][x]=[]


        print("for :",el)
        for i in range(5,-1,-1):
            print(i,"th floor :",town[i])
                
    

    
    
    
    
# 조건이 안들음.. 
def check(x,y,town,n): #현재 좌표의 설치된 모든 건설물이 성립 가능한지 체크한다
    for struct in town[y][x]:
        #기둥은 땅위 혹은 기둥(0)위 혹은 보의 끝에 설치할 수 있다.
        if struct ==0:
            if not (x==0 or (x-1>0 and 0 in town[x-1][y]) or(y-1 >0 and 1 in town[x][y-1])): 
                print("here1",x,y)
                return False
            
        elif struct ==1:
            if not ( (x-1>0 and 0 in town[x-1][y]) or (x-1>0 and y+1<n and 0 in town[x-1][y+1]) or (y-1>0 and 1 in town[x][y-1] and y+1<n and 1 in town[x][y+1]) ):
                print("here2",x,y)
                return False
        
        else :
            continue
            
            
    return True
            
                


    
n=5
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

solution(n,build_frame)    