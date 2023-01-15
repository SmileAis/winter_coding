from pprint import pprint
import copy
ans = []
a =0

# 모든 수 검사
def check_all(board:list):
    check_dict = {}
    for i in range(9):
        for j in range(9):
            if board[i][j] not in check_dict:
                check_dict[board[i][j]] = 0
            check_dict[board[i][j]] += 1
    print(check_dict)

    for i in range(1, 10):
        if i not in check_dict or check_dict[i] != 9:
            return False
    return True

# 그 줄에 없는 수 찾기
def find_num(row_num:int, board:list):
    tmp = []
    for i in range(1, 10):
        if i not in board[row_num]:
            tmp.append(i)
    return tmp

def check_low():
    return True

def check_col(num:int, row_num, col:int, board:list):
    for i in range(9):
        if board[row_num][col] == num:
            return False
    return True

def check_box(num, row_num, col, board):
    for i in range(row_num%3 +1):
        for j in range(col%3 +1):
            if board[i][j] == num:
                return False
    return True


def dfs(row_num:int, board:list):
    global a
    if check_all(board):
        return ans

    if a== 1:
        return

    else:
        nums = find_num(row_num, board)

        j = 0
        for i in range(9):
            if board[row_num][i] == 0:
                board[row_num][i] = nums[j]
            if check_col(nums[j], row_num, i, board) and check_box(nums[j], row_num, i, board):
                pprint(board)
                a+=1
                dfs(row_num, board)
                
                
                
            else:
                board[row_num][i] = 0
        dfs(row_num+1, board)
        
               
            
        print(nums)
        
        
    
    
    pass

def sol(board:list):
    global ans
    
    ans = copy.deepcopy(board)
    dfs(0, board)
    
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