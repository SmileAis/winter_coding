# 첫번째 부터 교환
# 이득이 되면 교환(서로 최소가 다른 과일)
# 최솟값이 2개 이상이면 교환x

def sol(fruit:list):
    ans = 0
    # 교환 리스트
    change_list = [0]*len(fruit)
    
    #각 최솟값 구하기
    min_list = list()
    for f in fruit:
        min_list.append(min(f))

    ans += sum(min_list)

    # 최솟값이 하나인지 확인
    for i in range(len(fruit)):
        count = 0

        for f in fruit[i]:
            if f == min_list[i] :
                count += 1
        if count > 1:
            change_list[i] = 1
    
    # 교환하기
    count = 0
    for i in range(len(fruit)-1):
        # 교환여부 확인
        if change_list[i] == 1:
            continue

        # 교환 적합 확인
        for j in range(1, len(fruit)):
            if change_list[j] == 1:
                continue 
            s_idx = fruit[i].index(min_list[i])
            l_idx = fruit[j].index(min_list[j])

            if abs(fruit[i][s_idx] - fruit[i][l_idx]) == 1:
                continue
            if abs(fruit[j][s_idx] - fruit[j][l_idx]) == 1:
                continue
            
            if s_idx != l_idx:
                count += 1
                change_list[i] = 1
                change_list[j] = 1
                break
                
    ans += count*2
    return ans



print(sol([[10, 20, 30], [12, 15, 20], [20, 12, 15], [15, 20, 10], [10, 15, 10]]))
print(sol([[10, 9, 11], [15, 20, 25]]))
print(sol([[0, 3, 27], [20, 5, 5], [19, 5, 6], [10, 10, 10], [15, 10, 5], [3, 7, 20]]))
print(sol([[3, 7, 20], [10, 15, 5], [19, 5, 6], [10, 10, 10], [15, 10, 5], [3, 7, 20], [12, 12, 6], [10, 20, 0], [5, 10, 15]]))