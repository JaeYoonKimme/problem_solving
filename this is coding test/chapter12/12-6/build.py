def solution(n, build_frame):
    town=[[[3]for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        town[0][i].append(2)

    #start
    for el in build_frame:
        x=el[0]
        y=el[1]
        a=el[2]
        b=el[3]
        
        #일단 새 명령을 추가하고 마지막에 전체 블록을 체크하자
        
        if b==1: #기둥이나 보를 추가하는 경우
            typ=check(town,x,y,a)
            if typ==0:
                town[x][y].append(0)
                town[x][y+1].append(0)
            elif typ==1:
                town[x][y].append(1)
                town[x+1][y].append(1)
            elif typ==-1:
                continue

        elif b==0:
            past_town=town
            if a==0: #기둥을 삭제하는 경우
                town[x][y].remove(0)
                town[x][y+1].remove(0)
            elif a==1: #보를 삭제하는 경우
                town[x][y].remove(1)
                town[x+1][y].remove(1)
                
            if remove_check(town)==False:
                town=past_town
            

    
    for i in range(5,-1,-1):
        print(i,"th floor :",town[i])
    for i in range(n+1):
        for j in range(n+1):
            for k in town[i][j]:
                if k ==1:
                    answer[i]
    answer = [[]]
    return answer

def check (town,x,y,a):
    if a==0: #기둥인경우
        if 3 in town[x][y] or 0 in town[x][y] or 1 in town[x][y]:
            return 0
        else :
            return -1

    elif a==1: #보인경우
        if 0 in town[x][y] or 0 in town[x+1][y] or (1 in town[x][y] and 1 in town[x+1][y]):
            return 1
        else :
            return -1

    else:
        return 3

def remove_check(town):
    for i in range(n+1):
        for j in range(n+1):
            for el in town[i][j]:
                if check(town,i,j,el)==-1:
                    return False
    return True


n=5
build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

solution(n,build_frame)
