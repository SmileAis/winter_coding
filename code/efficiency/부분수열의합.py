# 배열이 주어졌을 때 연속 부분 수열의 합이 홀수인 개수

def sol(nums:list):
    ans = 0
    count = [0]*2

    sum = 0
    for i in nums:
        sum += i
        
        if sum%2 == 1:
            ans += count[0]
            ans += 1    
        else:
            ans += count[1]
        count[sum%2] += 1
    return ans


print(sol([1,3,5]))
print(sol([2,4,6,8,10]))
print(sol([1, 2, 6, 2, 4, 3, 5, 3, 5, 3, 6, 3, 5, 4, 2, 3, 5, 1, 4, 3, 6]))
print(sol([100,99,98,90,55,33,23,45,56,7,8,12]))
print(sol([2,4,8]))