# tasks에 해야할 일의 시간이 주어진다.
# k에 정전이 일어나는 시간이 주어진다.
# 정전이 끝난 뒤 해야하는 작업의 위치를 구하라.

def sol(tasks:list, k:int):
    ans = 0

    zero_num = 0
    while(True):
        q = k // (len(tasks) - zero_num)
        r = k % (len(tasks) - zero_num)
        k = r

        for i in range(len(tasks)):
            if tasks[i] == 0:
                continue
            tasks[i] -= q

            if tasks[i] == 0:
                zero_num += 1
            if tasks[i] < 0:
                k -= tasks[i]
                tasks[i] = 0
                zero_num += 1
            
        print(tasks, k, zero_num)

        if zero_num == len(tasks): return -1
        if k >= len(tasks)-zero_num:
            continue
        break

  
    for i in range(len(tasks)):
        if tasks[i] == 0:
            continue
        if k == 0:
            ans = i+1
            break
        else:
            k -= 1

    return ans


print(sol([1, 2, 3], 5))
print(sol([8, 5, 2, 9, 10, 7], 30))
print(sol([8, 9, 12, 23, 45, 16, 25, 50], 100))
    