def sol(nums:list, m:int):
    ans = 0

    sum_dic = {}
    sum = 0
    for num in nums:
        sum += num

        if sum == m:
            ans += 1
        if sum-m in sum_dic:
            ans += sum_dic[sum-m]

        if sum in sum_dic:
            sum_dic[sum] += 1
        else:
            sum_dic[sum] = 1
            
    return ans


print(sol([1,2,3,-3,1,2,2,-3], 5))
print(sol([1,2,3,-3,1,2], 3))
print(sol([-1,0,1], 0))
print(sol([-1,-1,-1,1], 0))