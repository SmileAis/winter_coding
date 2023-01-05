# reports에 사람 이름과 사용 시간이 주어진다.
# times는 특정 범위의 시간이 주어진다.
# 시간 사이에 있는 사람들을 시간순으로 배열에 담아 리턴

def getMin(time:str):
    hour = int(time.split(":")[0])
    min = int(time.split(":")[1])

    return hour*60 + min

def sol(reports:list, times:str):
    ans =[]
    user_dict = {}
    ans_dict = {}

    for user in reports:
        name = user.split(" ")[0]
        time = user.split(" ")[1]
        min = getMin(time)

        user_dict[min] = name

    start = times.split(" ")[0]
    end = times.split(" ")[1]
    start_m = getMin(start)
    end_m = getMin(end)

    arr = []
    for key in user_dict:
        if key >= start_m and key <= end_m:
            arr.append(key)
    arr.sort()

    for i in arr:
        ans.append(user_dict[i])
    
    return ans


print(sol(["john 15:23", "daniel 09:30", "tom 07:23", "park 09:59", "luis 08:57"], "08:33 09:45"))
print(sol(["ami 12:56", "daniel 15:00", "bob 19:59", "luis 08:57", "bill 17:35", "tom 07:23", "john 15:23", "park 09:59"], 
          "15:01 19:59" ))