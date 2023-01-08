# k명이 가장 적은 움직임으로 모인다.
# 최소 이동 횟수?
# row와 col의 각 위치를 정렬한 후 중앙값에 모이는 것이 최소한의 움직임이다.

def sol(board:list):
    ans = 0

    rows = []
    cols = []
    # row/col 위치 저장
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                rows.append(row)
                cols.append(col)
    cols.sort()

    mid_row = rows[len(rows)//2]
    mid_col = cols[len(cols)//2]

    for i in range(len(rows)):
        ans += abs(mid_row - rows[i])
        ans += abs(mid_col - cols[i])
    
    return ans



print(sol([[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
print(sol([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]))
print(sol([[1, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1]]))