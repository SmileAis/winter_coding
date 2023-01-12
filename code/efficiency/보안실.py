def sol(reports:list, k:int):
    ans = []

    report_dict = {}
    
    for report in reports:
        name = report.split(" ")[0]
        time = report.split(" ")[1]

        h = time.split(":")[0]
        m = time.split(":")[1]
        total = int(h)*60 + int(m)

        if name not in report_dict:
            report_dict[name] = []
        report_dict[name].append(total)

    
    for name in report_dict:
        report_dict[name].sort()
        
        e_time = report_dict[name]
        print(name, e_time)
        left = 0
        tmp = []
        for right in range(len(e_time)):
            tmp.append(e_time[right])
            if e_time[right] - e_time[left] > 60:
                del tmp[0]
                left += 1
            print(name, tmp)
            if len(tmp) >= k:
                ans.append(name)
                break
    ans.sort()
    return ans

print(sol(["luis 08:11", "daniel 10:21", "luis 09:12", "emily 08:34", "luis 09:45", "luis 08:45", "luis 18:48", "emily 09:12", "daniel 11:15", "emily 09:34", "luis 10:35", "luis 10:45"], 3))

print(sol(["andew 08:11", "daniel 10:21", "luis 09:12", "emily 08:34", "luis 09:45", "andew 08:45", "luis 09:33", "andew 08:48", "emily 09:12", "daniel 11:15", "emily 09:35", "luis 09:35", "luis 10:45"], 4))

print(sol(["james 08:35", "james 08:50", "james 00:00"], 3))