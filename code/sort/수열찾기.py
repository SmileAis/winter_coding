# 수열이 주어진다.
# 이 수열은 기존 수열에 존재하는 원소들을 2배한 값들을 추가한 수열
# 원래 수열을 구하라

# 1. 정렬을 한 뒤 숫자가 몇번 나왔는지 딕셔너리에 기록
# 2. 작은수부터 순서대로 개수를 줄이고, 2배한 값의 개수도 줄이며 그 값을 ans에 추가한다.
# 3. 0은 pass

def sol(nums:list):
    ans = []
    count_nums = {}
    nums.sort()
    
    for num in nums:
        if num not in count_nums:
            count_nums[num] = 0
        count_nums[num] += 1
    print(count_nums)

    for num in nums:
        if count_nums[num] != 0:
            count_nums[num] -= 1
            count_nums[num*2] -= 1
            ans.append(num)

    return ans

print(sol([1, 10, 2, 3, 5, 6]))
print(sol([1,1,6,2,2,7,3,14]))
print(sol([14,4,2,6,3,10,10,5,5,7,7,14]))

    