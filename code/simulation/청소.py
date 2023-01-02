def sol(board:list, k:int):
    size = len(board)
    ans = [0, 0]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = 1
    
    for _ in range(k):
        mx = ans[0] + dx[dir]
        my = ans[1] + dy[dir]

        if mx < 0 or mx >= size or my < 0 or my >= size or board[mx][my]==1:
            dir = (dir + 1) % 4
            continue
        ans[0] = mx
        ans[1] = my
        
    return ans


# board = [[0, 0, 0, 0, 0],
#         [0, 1, 1, 0, 0],
#         [0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1],
#         [0, 0, 0, 0, 0]]
# k = 10

board = [[0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]
k = 20

print(sol(board, k))