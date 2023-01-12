def sol(s:str, k:int):
    ans = 9999999
    c_dict = {}
    left = 0
    
    for right in range(len(s)):
        if s[right] not in c_dict:
            c_dict[s[right]] = 0
        c_dict[s[right]] +=1
        # print(c_dict)
        
        while(len(c_dict) == k):
            ans = min(ans, right-left+1)
            c_dict[s[left]] -= 1
            
            if c_dict[s[left]] == 0:
                del c_dict[s[left]]
            left += 1
    
    return ans

print(sol("abacbbcdede", 5))
print(sol("acbbcdbbedeade", 4))
print(sol("abcabcabcbebef", 5))