def solution(n, build_frame):
    answer = []
    for structure in build_frame:
        x,y,a,b=structure
        if b==0:
            answer.remove([x,y,a])
            if check(answer)==False:
                answer.append([x,y,a])
        
        elif b==1:
            answer.append([x,y,a])
            if check(answer)==False:
                answer.remove([x,y,a])
        
    return sorted(answer)

def check(answer):
    for x,y,a in answer:
        if a==0: #기둥인경우
            if y==0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            else :
                return False
        
        elif a==1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else :
                return False
        
    return True


n=5
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n,build_frame))