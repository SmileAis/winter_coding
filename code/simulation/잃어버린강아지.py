def sol(board:list):
    ans = 0
    SIZE = 10

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    personDir, dogDir = 0, 0

    # 사람, 강아지의 위치 찾기
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 2:
                person = [i, j]
            if board[i][j] == 3:
                dog = [i, j]

    # 이동
    while(True):
        pIsBlocked, dIsBlocked = False, False
        pmx = person[0] + dx[personDir]
        pmy = person[1] + dy[personDir]
        if pmx < 0 or pmy < 0 or pmx >= SIZE or pmy >= SIZE or board[pmx][pmy] == 1:
            personDir = (personDir + 1) % 4
            pIsBlocked = True
        
            
        dmx = dog[0] + dx[dogDir]
        dmy = dog[1] + dy[dogDir]
        if dmx < 0 or dmy < 0 or dmx >= SIZE or dmy >= SIZE or board[dmx][dmy] == 1:
            dogDir = (dogDir + 1) % 4
            dIsBlocked = True

        if pIsBlocked==False:
            person[0] = pmx
            person[1] = pmy
        if dIsBlocked == False:
            dog[0] = dmx
            dog[1] = dmy

        print(person[0], person[1])
        print(dog[0], dog[1])
        ans += 1
        if person[0] == dog[0] and person[1] == dog[1]:
            break
    
    return ans


board = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 2, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0]]

board = [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 2, 1],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 3]
        ]


print(sol(board))