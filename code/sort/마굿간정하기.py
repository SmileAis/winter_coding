# n개의 마굿간이 수직선 상에 있다.
# c마리의 말을 최대한 멀리 배치하자.
# 그 거리를 반환

def sol(nums:list, c:int):
    ans = 0
    nums.sort()
    print(nums)

    left = 0
    right = max(nums)
    
    while(left <= right):
        count = 1
        idx = 0
        mid = (left + right) // 2
        for i in nums:
            if i - nums[idx] >= mid:
                count += 1
                idx = nums.index(i)
        if count >= c:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
        
    
    
    return ans

print(sol([1,2,8,4,9], 3))
print(sol([9,12,14,6,7], 4))
print(sol([5,12,34,16,18,23,29,15], 7))