def sol(s:str):
    ans = [0]*5

    dic = {}
    for i in range(5):
        dic[chr(ord('a')+i)] = 0

    for c in s:
        dic[c] += 1

    max = 0
    for i in dic:
        if max < dic[i]:
            max = dic[i]

    for i, j in enumerate(dic):
        ans[i] = max - dic[j]
        
    return ans


print(sol('aaabc'))
print(sol('aabb'))
print(sol('abcde'))
    