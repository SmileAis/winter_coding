from collections import deque

def sol(pool:list, a:int, b:int, home:int):
    visited = [[0, 0] for i in range(10001)]

    L = 1
    q = deque()
    visited[0][0] = 1
    visited[0][1] = 1
    for p in pool:
        visited[p][0] = 1
        visited[p][1] = 1
    q.append([a, 0])
    
    while q:
        l = len(q)
        for i in range(l):
            pos = q.popleft();
            if pos[0] == home:
                return L

            if pos[0]+a<10001 and visited[pos[0]+a][0] == 0:
                q.append([pos[0]+a, 0])
                visited[pos[0]+a][0] = 1
            if pos[0]-b > 0 and pos[1] == 0 and visited[pos[0]-b][1]==0:
                q.append([pos[0]-b, 1])
                visited[pos[0]-b][1] = 1
        L += 1
    return -1



print(sol([11,7,20], 3, 2, 10))
print(sol([1,15,11], 3, 2, 5))
print(sol([9,15,35,30,20], 2, 1, 25))
print(sol([5,12,7,19,23], 3, 5, 18))
print(sol([10,15,20], 3, 2, 2))