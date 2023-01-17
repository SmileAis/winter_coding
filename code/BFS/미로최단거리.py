from pprint import pprint
from collections import deque

def sol(board:list):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dist =[[0 for _ in range(7)]] * 7
    q = deque()
    L = 0
    q.append([0, 0])
    
    while q:
        l = len(q)
        L += 1
        
        for i in range(l):
            pos = q.popleft()

            for j in range(4):
                nx = pos[0] + dx[j]
                ny = pos[1] + dy[j]

                if nx >= 0 and nx < 7 and ny >=0 and ny < 7 and board[nx][ny] == 0:
                    board[nx][ny] = L
                    q.append([nx, ny])

    if board[6][6] != 0:
        return board[6][6]
        
    return -1


print(sol([[0, 0, 0, 0, 0, 0, 0], 
           [0, 1, 1, 1, 1, 1, 0], 
           [0, 0, 0, 1, 0, 0, 0], 
           [1, 1, 0, 1, 0, 1, 1], 
           [1, 1, 0, 1, 0, 0, 0], 
           [1, 0, 0, 0, 1, 0, 0], 
           [1, 0, 1, 0, 0, 0, 0]]))

print(sol([[0, 0, 0, 0, 0, 0, 0], 
           [0, 1, 1, 1, 1, 1, 0], 
           [0, 0, 0, 1, 0, 0, 0], 
           [1, 1, 0, 1, 1, 1, 1], 
           [1, 1, 0, 1, 0, 0, 0], 
           [1, 0, 0, 0, 1, 0, 0], 
           [1, 0, 1, 0, 1, 0, 0]]))