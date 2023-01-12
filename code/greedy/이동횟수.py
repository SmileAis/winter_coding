def sol(nums:list):
    ans = 0

    # 박스 개수 세기
    box_dict = {2:0, 3:0}
    for num in nums:
        if num == 4 or num == 5:
            ans += 1
            continue
        box_dict[num] += 1
    print(box_dict, ans)

    if box_dict[2] == box_dict[3]:
        ans += box_dict[2]
    elif box_dict[2] < box_dict[3]:
        ans += box_dict[3]
    else:
        ans += box_dict[3]
        box_dict[2] -= box_dict[3]
        if box_dict[2] > 0:
            ans += box_dict[2]//2 + 1
    
    return ans


print(sol([2,5,3,4,2,3]))
print(sol([2,3,4,5]))
print(sol([3,3,3,3,3]))