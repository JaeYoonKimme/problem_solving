def solution(n, lost, reserve):
    answer = 0
    uniform=[1]*(n+1)
    for x in lost:
        uniform[x]=uniform[x]-1
    for x in reserve:
        uniform[x]=uniform[x]+1

    for i in range(1,n):
        if uniform[i]==2 and uniform[i+1]==0:
            uniform[i]=uniform[i]-1
            uniform[i+1]=uniform[i+1]+1
        elif uniform[i]==0 and uniform[i+1]==2:
            uniform[i]=uniform[i]+1
            uniform[i+1]=uniform[i+1]-1
    for i in range(1,n+1):
        if uniform[i]>0:
            answer=answer+1
    return answer


n=5
lost=[1,3]
reserve=[2,4,5]

print(solution(n,lost,reserve))