def sol(votes:list, k:int):
    # 딕셔너리에 추가
    voted_dict = {}
    for vote in votes:
        voter = vote.split(" ")[0]
        candidate = vote.split(" ")[1]
        if candidate not in voted_dict :
            voted_dict[candidate] = []
        voted_dict[candidate].append(voter)
    print(voted_dict)

    # k표 이상 확인
    count_voter = {}
    for voted in voted_dict:
        if len(voted_dict[voted]) >= k:
            for i in range(len(voted_dict[voted])):
                if voted_dict[voted][i] not in count_voter:
                    count_voter[voted_dict[voted][i]] = 1
                else:
                    count_voter[voted_dict[voted][i]] += 1
    print(voted_dict)
    print(count_voter)

    m = max(list(count_voter.values()))
    ansList = list()
    for voter in count_voter:
        if count_voter[voter] == m:
            ansList.append(voter)
    ansList.sort()
    
    result = ansList[0]
    return result


print(sol(["john tom", "daniel luis", "john luis", "luis tom","daniel tom", "luis john"], 2))
print(sol(["john tom", "park luis", "john luis", "luis tom", "park tom", "luis john",
           "luis park", "park john", "john park", "tom john", "tom park", "tom luis"], 3))