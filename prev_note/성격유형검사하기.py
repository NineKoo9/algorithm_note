def solution(surveys, choices):
    mbti_table = [{"R":0, "T":0},
              {"C":0, "F":0},
              {"J":0, "M":0},
              {"A":0, "N":0}]
    row_idxs = {"RT":0, "TR":0,
               "CF":1, "FC":1,
               "JM":2, "MJ":2,
               "AN":3, "NA":3}
    
    N = len(surveys)
    select_score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    for i in range(N):
        idx = row_idxs[surveys[i]]
        type_1, type_2 = surveys[i][0], surveys[i][1]
        choice = choices[i]
        if choice == 4:
            continue
        if choice < 4:
            # 타입 1에 해당하는 값이 올라가야 한다.
            mbti_table[idx][type_1] += select_score[choice]
        else:
            mbti_table[idx][type_2] += select_score[choice]
    answer = ""
    for mbti_row in mbti_table:
        # 여기서 둘중에 하나를 선택해서 answer 에 붙여줘야지
        t1, t2 = sorted(mbti_row.items(), key=lambda t:(-t[1], t[0]))
        answer += t1[0]
    return answer