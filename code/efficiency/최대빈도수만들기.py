def sol(nums:list, k:int):
    ans = 0
    nums.sort()

    left = 0
    sum = 0
    for right in range(len(nums)):
        sum += nums[right]

        while(sum+k < nums[right]*(right-left+1)):
                sum -= nums[left]
                left += 1
        ans = max(ans, right-left+1)
                

    return ans

print(sol([1,2,4,7], 5))
print(sol([5,7,8,2,9,6,3], 10))
print(sol([6,8,1,3,12,9,10], 10))