def sol(nums:list, m:int):
    ans = 0
    left = 0
    right = len(nums)-1

    nums.sort()
    print(nums)
    while(left <= right):
        mid = (right+left)//2

        if nums[mid] == m:
            ans = mid+1
            break
        if nums[mid] > m:
            right = mid-1
        elif nums[mid] < m:
            left = mid+1

    return ans

print(sol([23, 87, 65, 12, 57, 32, 99, 81], 32))
    