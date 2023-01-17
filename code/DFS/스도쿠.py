from pprint import pprint

ans = [[0 for i in range(9)] for j in range(9)]
zero_points = []
chkCol = []
chkRow = []
chkBox = []
cnt = 0

def getBoxNum(i, j):
    return (i//3) * 3 + (j//3)

def dfs(L, board:list):
    global ans

    print(L)
    if cnt == L:
        pprint(1)
        for i in range(9):
            for j in range(9):
                ans[i][j] = board[i][j]
        return
    # 9까지 반복문 돌면서 chkRow. chkCol, chkBox에 없으면 넣기
    # 있으면 다시 0으로
    else:
        x = zero_points[L][0]
        y = zero_points[L][1]
        box = getBoxNum(x, y)
        
        for i in range(1, 10):
            if chkRow[x][i] == 0 and chkCol[y][i] == 0 and chkBox[box][i] == 0:
                board[x][y] = i
                chkRow[x][i] = chkCol[y][i] = chkBox[box][i] = 1
                dfs(L+1, board)
                board[x][y] = 0
                chkRow[x][i] = chkCol[y][i] = chkBox[box][i] = 0 
        

def sol(board:list):
    global zero_points, chkBox, chkCol, chkRow, cnt

    chkCol = [[0 for i in range(10)] for i in range(9)]
    chkRow = [[0 for i in range(10)] for i in range(9)] 
    chkBox = [[0 for i in range(10)] for i in range(9)]
    
    # 모든 0의 좌표 구하고 사용한 숫자 체크하기
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                zero_points.append([i, j])
                cnt+=1
            else:
                chkRow[i][board[i][j]] = 1
                chkCol[j][board[i][j]] = 1
                chkBox[getBoxNum(i, j)][board[i][j]] = 1

    print(zero_points)
    dfs(0, board)

    pprint(ans)
    return ans

    
sol([[0, 2, 3, 0, 5, 0, 7, 8, 9], 
           [0, 5, 6, 0, 8, 9, 1, 0, 3], 
           [0, 8, 9, 1, 0, 3, 0, 5, 6], 
           [0, 1, 0, 0, 6, 0, 8, 9, 0], 
           [3, 0, 5, 0, 9, 7, 0, 1, 4], 
           [0, 9, 7, 0, 1, 0, 0, 6, 5], 
           [5, 3, 0, 6, 0, 2, 9, 7, 8], 
           [6, 0, 2, 9, 0, 8, 5, 3, 1], 
           [9, 0, 8, 0, 3, 0, 6, 0, 2]])