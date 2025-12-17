def solution(id_list, report, k):
    # 각 유저별로 처리 결과 메일을 받은 "횟수"를 리턴
    # 1. 각 유저별로 신고한 기록을 적는다.
    # 2. 신고한 기록에서 k이상인 녀석은 밴을 먹인다.
    # 3.
    id_dic = {id: 0 for id in id_list}
    complainee_id_dic = {id: [] for id in id_list}  # 여기는 특정 닉네임을 신고한 사람을 기록한다.
    ban_count = {id: 0 for id in id_list}
    for s in report:
        complainer, complainee = s.split(" ")
        if complainer not in complainee_id_dic[complainee]:
            complainee_id_dic[complainee].append(complainer)
            ban_count[complainee] += 1

    ban_id_lst = []
    for user_id, count in ban_count.items():
        if count >= k:
            ban_id_lst.append(user_id)
    for ban_id in ban_id_lst:
        for complainer in complainee_id_dic[ban_id]:
            id_dic[complainer] += 1
    return list(id_dic.values())

