def solution(records):    
    status_dic = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}    
    uid_name_dic = {}
    results = []
    for record in records:
        status, *info = record.split(" ")
        if status != "Change":
            results.append((status, info[0]))
        if status != "Leave":
            uid_name_dic[info[0]] = info[1]
    answer = [f"{uid_name_dic[uid]}님이 {status_dic[status]}" for status, uid in results]
    
    return answer