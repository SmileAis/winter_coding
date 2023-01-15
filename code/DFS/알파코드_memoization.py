import time

stime= time.time()
res = 0
memo = []

def dfs(start:int, s:str):
    global res

    if memo[start] > 0:
        return memo[start]
    if start<len(s) and s[start] =='0':
        return 0
    if start == len(s) or start == len(s)-1:
        return 1
        
    else:
        res = dfs(start+1, s)
        tmp = int(s[start:start+2])
        if tmp <= 26:
            res += dfs(start+2, s)
        memo[start] = res
        return memo[start]
            
def sol(s:str):
    global res, memo
    res = 0 
    memo = [0] *101
    
    ans = dfs(0, s)
    print(memo)
    return ans


# print(sol("25114"))
# print(sol("23241232"))
# print(sol("21020132"))
print(sol("21350"))
# print(sol("120225"))
# print(sol("232012521"))
etime = time.time()

print(etime-stime)
    