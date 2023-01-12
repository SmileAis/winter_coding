def sol(plantTime:list, growTime:list):
    ans = 0

    total = [plantTime[i] + growTime[i] for i in range(len(plantTime))]
    print(total)
    
    idx = total.index(max(total))
    
    total[idx] = 0
    ans += plantTime[idx]

    planted_idx = [idx]
    
    while(True):
        idx = total.index(max(total))
        total[idx] = 0
        ans += plantTime[idx]

        if max(total) == 0:
            break
        
        for i in planted_idx:
            if growTime[i] == 0:
                continue
            growTime[i] -= plantTime[idx]
            if growTime[i] <= 0:
                growTime[i] = 0
    ans += growTime[idx]
        
        
    
    return ans


print(sol([1,3,2], [2,3,2]))
print(sol([2,1,4,3], [2,5,3,1]))
print(sol([1,1,1], [7,3,2]))
print(sol([5,7,10,15,7,3,5], [6,7,2,10,15,6,7]))
print(sol([1,2,3,4,5,6,7],[7,5,4,3,2,1,6]))