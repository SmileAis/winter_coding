# 팰린드롬의 모든 경우 구하기

res = ""
c_dict ={}
ans = []
def dfs(s):
    global res, c_dict, ans
            
    if len(res) == len(s):
        ans.append(res)
        return

    else:
        for key in c_dict:
            if c_dict[key] != 0:
                res = key + res + key
                c_dict[key] -= 2
            else:
                continue
            dfs(s)
            c_dict[res[0]] += 2
            res = res[1:-1]
            

def sol(s:str):
    global res, c_dict, ans
    ans = []
    c_dict = {}
    
    # 각 문자 개수 파악하기
    for chr in s:
        if chr not in c_dict:
            c_dict[chr] = 0
        c_dict[chr] += 1

    # 팰린드롬의 경우 홀수가 없거나 하나
    odd_chr = '!'
    odd_count = 0
    for key in c_dict:    
        if c_dict[key] % 2 == 1:
            odd_count += 1
            odd_chr = key;

    # 홀수가 2개 이상인경우 
    if odd_count > 1:
        return []

    res = ""
    if odd_chr != '!':
        res += odd_chr
        c_dict[odd_chr] -= 1
    dfs(s)
    
    return ans

print(sol("aaaabb"))
print(sol("abbcc"))
print(sol("abbccee"))
print(sol("abbcceee"))