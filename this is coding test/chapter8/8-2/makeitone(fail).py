list=[]
d= [0]*30001

def makeitone(x,count):
    if x<=1:
        list.append(count)
        return

    if x%5 ==0:
        makeitone(x//5,count+1)

    if x%3 ==0:
        makeitone(x//3,count+1)

    if x%2 ==0:
        makeitone(x//2,count+1)

    makeitone(x-1,count+1)
    
makeitone(250,0)
print(min(list))
#답은 도출할 수 있는 풀이이지만 값이 커지면 시간이 기하급수적으로 증가한다 ->실패 