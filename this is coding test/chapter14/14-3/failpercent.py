def solution(N, stages):
    answer = []
    stages.sort()
    result=[]
    for stageNum in range(1,N+1):
        reached=0
        notCleared=0
        for player in stages:
            if player>=stageNum:
                reached+=1
            if player==stageNum:
                notCleared+=1
        if reached==0:
            result.append((0,stageNum))
        else:
            failpercent= notCleared/reached
            #print(failpercent)
            result.append( (failpercent,stageNum) )
        
    result=sorted(result, key=lambda x : (-x[0], x[1]) )
    for i in result:
        answer.append(i[1])
    return answer



N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N,stages))