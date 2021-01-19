def solution(n, weak, dist):
    answer = 0
    clock=[0]*n
    dist=sorted(dist,reverse=True)
    for p in weak:
        clock[p]=1
    for i in range(12):
        clock[i]=i

    index=0
    for worker in dist:
        for startpoint in weak:
            index=startpoint
            blank=[]
            for i in range(worker):
                index+=1
                if index>12:
                    index-=12
                elif index<0:
                    index+=12
                
                if clock[index]==1:
                    blank.append(index)

                

                


    
            







weak=[1,5,6,10]
dist=[1,2,3,4]
n=12

print(solution(n,weak,dist))