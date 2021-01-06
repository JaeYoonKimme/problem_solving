from collections import deque
import copy

n=int(input())
indegree=[0]*(n+1)
time=[0]*(n+1)
graph=[[]for i in range(n+1)]

for i in range(1,n+1):
    data=list(map(int,input().split()))
    time[i]=data[0]

    for x in data[1:-1]: #맨 뒤에서 두번째원소부터 두번째 원소까지..
        indegree[i]=indegree[i]+1
        graph[x].append(i)

def topology_sort():
    q=deque()
    result=copy.deepcopy(time)
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now=q.popleft()
        for i in graph[now]:
             indegree[i]=indegree[i]-1
             result[i]=max(result[i], time[i]+result[now])
             if indegree[i]==0:
                 q.append(i)
            

    for i in range(1,n+1):
        print(result[i])


topology_sort()

#문제를 똑바로 이해하고 풀도록 하자..