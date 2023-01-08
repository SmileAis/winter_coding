def sol(nums:list):
    ans = []
    binary_dict = {}
    
    # nums 배열 오름차순 정렬하기
    nums.sort()

    # 작은순부터 2진수 1개수 구해 dict 1개수, 숫자 리스트
    for num in nums:
        binary = ""
        count = 0

        n = num
        while(n // 2 != 0):
            if n%2 == 1:
                count += 1
            n = n//2
        count += 1
        print(count)

        if count not in binary_dict:
            binary_dict[count] = [num]
        else:
            binary_dict[count].append(num)

    print(binary_dict)
        
    # dict에 저장된 리스트 정렬 후 하나씩 asn에 추가하기
    for i in range(1000):
        if i in binary_dict:
            binary_dict[i].sort()
            for j in binary_dict[i]:
                ans.append(j)
    
    return ans


print(sol([5, 6, 7, 8, 9] ))
print(sol([5, 4, 3, 2, 1] ))
print(sol([12, 5, 7, 23, 45, 21, 17] ))
