from collections import deque

def sol(s:int, e:int):
    ans = 0
    visited = [[0, 0] for _ in range(200001)]

    q = deque()
    q.append(s)
    L = 0
    visited[s][0] = 1
    while q:
        l = len(q)
        L += 1
        
        for i in range(l):
            # print(q)
            pos = q.popleft()

            for next_pos in [pos+1, pos-1, pos*2]:
                # print(next_pos, L%2)
                if next_pos < 200001 and next_pos >= 0 and visited[next_pos][L%2] == 0:
                    q.append(next_pos)
                    visited[next_pos][L%2] = 1
        e += L

        if e>200000:
            return -1

        if visited[e][L%2]==1:
            return L
            

    return -1


print(sol(1, 11))
print(sol(10, 3))
print(sol(1, 34567))
print(sol(5 ,6))
print(sol(2, 54321))