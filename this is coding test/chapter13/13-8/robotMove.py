from collections import deque

def solution(board):
    n=len(board)
    new_board=[[1]*(n+2) for i in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1]=board[i][j]
    
    q=deque()
    visited=[]
    pos={(1,1),(1,2)}
    q.append((pos,0))
    visited.append(pos)

    while q:
        pos, cost= q.popleft()
        if (n,n) in pos:
            return cost
        
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                visited.append(next_pos)
                q.append((next_pos,cost+1))

    return 0





def get_next_pos(pos, new_board):
    result_pos=[]

    dx=[0,1,0,-1]
    dy=[-1,0,1,0]
    pos = list(pos)
    pos1x,pos1y,pos2x,pos2y = pos[0][0],pos[0][1],pos[1][0],pos[1][1]

    for i in range(4):
       next_pos1x=pos1x+dx[i]
       next_pos1y=pos1y+dy[i]
       next_pos2x=pos2x+dx[i]
       next_pos2y=pos2y+dy[i]

       if new_board[next_pos1x][next_pos1y]== 0 and new_board[next_pos2x][next_pos2y]==0 :
           result_pos.append(  {(next_pos1x,next_pos1y),(next_pos2x,next_pos2y)}  )

    if pos1x==pos2x:
        for i in [-1,1]:
            if new_board[pos1x+i][pos1y]==0 and new_board[pos2x+i][pos2y]==0:
                result_pos.append({(pos1x,pos1y),(pos1x+i, pos1y)})
                result_pos.append({(pos2x,pos2y),(pos2x+i, pos2y)})
    
    elif pos1y==pos2y:
        for i in [-1,1]:
            if new_board[pos1x][pos1y+i]==0 and new_board[pos2x][pos2y+i]==0:
                result_pos.append( {(pos1x,pos1y), (pos1x, pos1y+i) } )
                result_pos.append( {(pos2x,pos2y), (pos2x, pos2y+i) } )


    return result_pos





board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))