from collections import deque
from pprint import pprint
import copy

b_size = 0
dist = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def sol(board:list):
    global b_size, dist
    b_size = len(board)
    dist = [[0 for _ in range(b_size)] for _ in range(b_size)]
    ans = 99999
    
    q = deque()
    
    for i in range(b_size):
        for j in range(b_size):
            if board[i][j] == 1:
                chk = copy.deepcopy(board)
                q.append([i, j])
                L = 0
                while q:
                    L+=1
                    l = len(q)

                    for ii in range(l):
                        pos = q.popleft()
                        x = pos[0]
                        y = pos[1]
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
        
                            if nx >= 0 and nx < b_size and ny >= 0 and ny < b_size and board[nx][ny] == 0:
                                if chk[nx][ny] == 0:
                                    chk[nx][ny] = 1
                                    dist[nx][ny] += L
                                    q.append([nx, ny])
                                                
    pprint(dist)
    
    for i in range(b_size):
        for j in range(b_size):
            if dist[i][j] != 0 and ans > dist[i][j]:
                ans = dist[i][j]
    
    return ans


print(sol([[1, 0, 2, 0, 1], 
           [0, 0, 0, 0, 0], 
           [0, 0, 1, 0, 0], 
           [0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0]]))
print(sol([[1, 0, 0, 0, 1], 
           [0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0], 
           [0, 0, 0, 1, 0]] ))
print(sol([[1, 0, 0, 0, 1, 1], 
           [0, 1, 0, 0, 1, 0], 
           [0, 1, 0, 0, 0, 0], 
           [0, 0, 0, 0, 1, 0], 
           [0, 0, 0, 0, 0, 1], 
           [1, 0, 0, 0, 1, 1]]))