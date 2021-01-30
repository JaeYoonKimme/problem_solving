from itertools import combinations
import copy

n=int(input())
hallway=[]
for i in range(n):
    hallway.append(list(map(str,input().split())))

def isStudentHideWell(row,col,hall,direction):
    if row<0 or row>n-1 or col<0 or col>n-1:
        return True
    if hall[row][col]=="O":
        return True
    if hall[row][col]=="S":
        return False
    #if hall[row][col]=="T":
    #    return True
    
    if direction==0:
        if not isStudentHideWell(row,col+1,hall,1):
            return False
        if not isStudentHideWell(row,col-1,hall,2):
            return False
        if not isStudentHideWell(row+1,col,hall,3):
            return False
        if not isStudentHideWell(row-1,col,hall,4):
            return False
        return True
    
    elif direction==1:
        return isStudentHideWell(row,col+1,hall,1)
    elif direction==2:
        return isStudentHideWell(row,col-1,hall,2)
    elif direction==3:
        return isStudentHideWell(row+1,col,hall,3)
    elif direction==4:
        return isStudentHideWell(row-1,col,hall,4)

    

locationOfTeacher=[]
locationOfEmptySpace=[]
for i in range(n):
    for j in range(n):
        if hallway[i][j]=="T":
            locationOfTeacher.append((i,j))
        elif hallway[i][j]=="X":
            locationOfEmptySpace.append((i,j))

newWall=list(combinations(locationOfEmptySpace,3))


result=False
for construct in newWall:
    newHallway=copy.deepcopy(hallway)
    for wall in construct:
        newHallway[wall[0]][wall[1]]="O"
    
    teachergo=True
    for teacher in locationOfTeacher:
        if isStudentHideWell(teacher[0],teacher[1],newHallway,0)==False:
            teachergo=False
    
    if teachergo==True:
        result=True
        
        


if result==True:
    print("YES")
else:
    print("NO")
    
#이 문제는 진작에 맞았는데 출력을 대문자로 안해줘서 틀리고 있었다. 
    


