import time
stime = time.time()
ans = []
res = ""
res_list = []

def dfs(start:int, s:str):
    global res, res_list
    if len(res_list) > 4: 
        return

    if len(res_list)==4 and start == len(s):
        ans.append(".".join(res_list))
        return

    else:
        for i in range(start, len(s)):
            cur_ip = s[start:i+1]
            # 예외) 255 이상
            if int(cur_ip) > 255:
                return
            # 예외) 0으로 시작
            if cur_ip[0]=='0' and len(cur_ip) >1:
                return

            res_list.append(cur_ip)
            dfs(i+1, s)
            res_list = res_list[:-1]
                   

def sol(s:str):
    global ans
    ans = []
    # 예외처리(12자리 이상 IP)
    if len(s) > 12:
        return []
    # 예외처리(4자리 IP)
    if len(s) == 4:
        res = ".".join(s)
        ans.append(res)
        return ans
    else:
        dfs(0, s)
        
    return ans


print(sol("1234"))
print(sol("2025505"))
print(sol("0000"))
print(sol("255003"))
print(sol("155032012"))
etime = time.time()

print(etime-stime)