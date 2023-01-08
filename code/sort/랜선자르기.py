# 범위 생각하기
# 이진탐색으로 최대 길이 찾기

def sol(nums:list, n:int):
    left = 1
    right = max(nums)
    
    while(left <= right):
        count = 0
        mid = (left + right)//2
        for num in nums:
            count += num//mid

        # print(mid)
        
        if count > n:
            left = mid + 1
        elif count < n:
            right = mid -1
        else:
            ans = mid
            left = mid +1
            
    return ans

print(sol([802, 743, 457, 539], 11))
print(sol([8593, 9617, 9313, 4513, 7505, 5457, 8257, 4689, 2657], 100))
print(sol([93, 97, 93, 53, 75, 57, 85, 89, 67], 30))