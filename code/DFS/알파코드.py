import time

stime= time.time()
res = 0

def dfs(start:int, s:str):
    global res
    
    if start == len(s):
        res += 1
        
    else:
        for i in range(start, len(s)):
            # 예외처리 26보다 큰 경우
            if int(s[start:i+1]) > 26:
                return
            # 0이거나 0으로 시작
            if int(s[start:i+1][0]) == 0:
                return
            dfs(i+1, s)     
            
def sol(s:str):
    global res
    res = 0 
    
    dfs(0, s)
    ans = res
    return ans


print(sol("25114"))
print(sol("23241232"))
print(sol("21020132"))
print(sol("21350"))
print(sol("120225"))
print(sol("232012521"))
etime = time.time()

print(etime-stime)
    