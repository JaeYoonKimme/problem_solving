'''
def solution(name):
    answer = 0
    for x in name:
        answer=answer+min( (ord(x)-ord("A")) , (ord("Z")-ord(x)+1) )
    answer=answer+(len(name)-1)
    return answer
'''

def solution(name):
    answer=0
    index=0
    size=len(name)
    namelst=list(name)
    goal=["A"]*size
    while True:
        if namelst==goal:
            break

        if namelst[index]!="A":
            answer=answer+min( (ord(namelst[index])-ord("A")) , (ord("Z")-ord(namelst[index])+1) )
            namelst[index]="A"
            print(namelst[index])
            print(answer)
        
        if namelst==goal:
            break
        
        
        step=99999
        next_index=0
        for i in range(size):
            if namelst[i]!="A" :
                bothstep=min(i-index,size-i)
                step=min(step,bothstep)
        next_index=index+step
        next_index=next_index%size
        
        if namelst[next_index]!="A":
            index=next_index
            answer=answer+step
        else :
            index=size-step
            answer=answer+step
        print(answer)




    return(answer)
        

 

name="JEROEN"
print(solution(name))
#커서가 역행이 가능한걸 고려하지 않은 경우 위의 풀이로 가능하다.. 