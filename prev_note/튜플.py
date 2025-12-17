def solution(s):
    s = s[1:-1] # "{20,111},{111}" 이렇게 생긴 문자열을 처리해야 하는 구나...
    temp = ""
    s_lst = []
    for ch in s:
        if (len(temp) == 0 and ch == ",") or ch == "{":
            continue
        if ch == "}":
            s_lst.append(temp.split(","))
            temp = ""
            continue
        temp += ch
    s_lst.sort(key=lambda x: len(x))
    print(s_lst) # [['3'], ['2', '3'], ['4', '2', '3'], ['2', '3', '4', '1']]
    answer = [int(s_lst[0][0])]
    for idx, sub_s in enumerate(s_lst[:-1]):
        n_sub_s = s_lst[idx+1]
        n = set(n_sub_s) - set(sub_s)
        answer.append(int(n.pop()))
    print(answer)


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
# print(solution("{{20,111},{111}}"))
# 문자열 처리하는 방법이 흥미롭군...
# 자료구조 set을 어떻게하면 깔끔하게 숫자로 바꾸지?