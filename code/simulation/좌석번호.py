from pprint import pprint

def sol(c:int, r:int, k:int):
    ans = [0,-1]

    seats = [[0 for _ in range(r)] for _ in range(c)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = 1

    #사람이 더 많은경우
    if c*r < k:
        ans = [0, 0]
        return ans

    # 좌석 세팅
    count = 0
    while(count < k):
        mc = ans[0] + dx[dir]
        mr = ans[1] + dy[dir]
        print(mc, mr)
        if mc < 0 or mr < 0 or mc >= c or mr >= r or seats[mc][mr] == 1:
            dir = (dir + 1) % 4
            continue
            
        seats[mc][mr] = 1
        ans[0] = mc
        ans[1] = mr
        count += 1  
        pprint(seats)

    ans[1] += 1
    ans[0] += 1
    return ans

pprint(sol(6,5,12))
    