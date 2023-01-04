def sol(s:str):
    ans = 0

    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    print(dic)

    num_set = set()
    for i in dic:
        while dic[i] in num_set:
            ans += 1
            dic[i] -= 1
        else:
            if(dic[i] == 0):
                continue
            num_set.add(dic[i])
        

    return ans


print(sol("aaabbbcc"))
print(sol('aaabbc'))
print(sol('aebbbc'))
print(sol('aaabbbccde'))
    