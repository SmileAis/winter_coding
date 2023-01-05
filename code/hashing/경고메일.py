# reports에 이름/시간/입장 or 퇴장
# time은 이용 시간 제한.
# 이용시간이 넘은 사람들 반환

# in_dict와 out_dict를 만들기 
# -> in_dict/out_dict 시간:이름으로 넣기
# -> out_dict에 값을 넣을 때 바로 시간을 계산해서 time을 초과했으면 답에 추가하기
# 이용시간을 저장할 dict 하나 더 생성해서 시간 누적.

def getMin(time:str):
    hour= int(time.split(":")[0])
    min = int(time.split(":")[1])

    return hour*60 + min

    
def sol(reports:list, time:int):
    ans = []
    in_dict = {}
    timer_dict = {}

    for report in reports:
        name = report.split(" ")[0]
        t = report.split(" ")[1]
        mode = report.split(" ")[2]

        min = getMin(t)
        if mode == "in":
            in_dict[name] = min
        elif mode == "out":
            using_time = min - in_dict[name]
            if name not in timer_dict:
                timer_dict[name] = using_time
            else:
                timer_dict[name] += using_time
    print(timer_dict)

    for key in timer_dict:
        if timer_dict[key] > time:
            ans.append(key)
    
    ans.sort()

    return ans


print(sol(["john 09:30 in", "daniel 10:05 in", "john 10:15 out", "luis 11:57 in", "john 12:03 in",
           "john 12:20 out", "luis 12:35 out", "daniel 15:05 out"], 60))
print(sol(["bill 09:30 in", "daniel 10:00 in", "bill 11:15 out", "luis 11:57 in", "john 12:03 in",
           "john 12:20 out", "luis 14:35 out", "daniel 14:55 out"], 120))