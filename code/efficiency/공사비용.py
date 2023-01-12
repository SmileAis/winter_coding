def sol(cost:list, m:int):
    ans = 0

    left = 0
    sum = 0
    for right in range(len(cost)):
        sum += cost[right]

        while(sum > m):
            sum -= cost[left]
            left += 1
        
        ans = max(ans, right-left + 1)
            
    return ans


print(sol([0, 150, 100, 0, 150, 0, 70, 140], 350))
print(sol([100, 200, 300, 400, 500, 100], 300))
print(sol([100, 200, 300, 400, 0, 100, 150, 500, 100], 300))