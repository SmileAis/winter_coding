from pprint import pprint

def sol(keypad:list, password:str):
    ans = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    dist = [[2]*9 for i in range(9)]
    # pprint(dist)
    
    # pad생성
    pad = [[0]*3 for _ in range(3)]
    for i in range(9):
        pad[i//3][i%3] = keypad[i] 
    # pprint(pad)

    for i in range(9):
        dist[i][i] = 0
    
    # memorize
    for i in range(3):
        for j in range(3):
            for k in range(8):
                mx = i + dx[k]
                my = j + dy[k]

                if mx <0 or my < 0 or mx > 2 or my >2:
                    continue

                start = pad[i][j]
                dest = pad[mx][my]
                dist[start-1][dest-1] = 1
    # pprint(dist)

    for i in range(len(password)-1):
        s = int(password[i])-1
        d = int(password[i+1])-1

        ans += dist[s][d]
    
    return ans


print(sol([2,5,3,7,1,6,4,9,8], '7596218'))
print(sol([1,5,7,3,2,8,9,4,6], '63855526592'))
print(sol([2,9,3,7,8,6,4,5,1], '323254677'))
print(sol([1,6,7,3,8,9,4,5,2], '3337772122'))