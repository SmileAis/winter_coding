def sol(nums:list):
    ans = [""]*len(nums)

    # nums list 하나씩 가져오기
    for i in range(len(nums)):
        num = nums[i]-1
        t = 1

        for j in range(1, 9999999):
            if num >= t*9:
                num -= t*9
            else:
                l = (j+1)//2
                res = [0]*100
                pal = ''
                res[0] = 1

                for k in range(l):
                    res[k] += num // t
                    pal += str(res[k])
                    num %= t
                    t = t//10
                for k in range(l - j%2 -1, -1, -1):
                    pal += str(res[k])
                ans[i] = pal
                break
            if j % 2 == 0:
                t *= 10
    return ans

print(sol([1, 12, 24]))