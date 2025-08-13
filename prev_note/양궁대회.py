def calc_point(apeach, lion):  # 점수를 리턴하자
    apeach_point = 0
    lion_point = 0
    for i in range(11):
        apeach_arrow = apeach[i]
        lion_arrow = lion[i]
        if apeach_arrow > lion_arrow or (apeach_arrow != 0 and apeach_arrow == lion_arrow):
            apeach_point += (10 - i)
        elif apeach_arrow < lion_arrow:
            lion_point += (10 - i)
    return (apeach_point, lion_point)


def solution(n, info):
    from functools import cmp_to_key

    def compare_answer(a, b):
        if a[0] > b[0]:
            return -1
        elif a[0] == b[0]:
            reverse_a = a[1][::-1]
            reverse_b = b[1][::-1]
            for i in range(11):
                if reverse_a[i] > reverse_b[i]:
                    return -1
                elif reverse_a[i] < reverse_b[i]:
                    return 1
            return 0
        else:
            return 1

    # 예제 4번이 문제네...
    def dfs(lion, n, start):  # 어쨋든 라이언이 이기는 경우는 값이 더 커야겠네?
        if n == 0:
            # 이제 점수를 계산해서
            apeach_point, lion_point = calc_point(info, lion)
            if apeach_point < lion_point:
                diff = lion_point - apeach_point
                answers.append((diff, lion))
            return
        for i in range(start, 11):  # 이기지 못하면 안쏘는게 맞겠네?
            apeach_point = info[i]
            if n >= apeach_point + 1:
                lion[i] = apeach_point + 1
                dfs(lion.copy(), n - lion[i], i + 1)
                lion[i] = 0

    answers = []
    dfs([0] * 11, n, 0)
    answers.sort(key=cmp_to_key(compare_answer))
    # 뭐가 되게 중복된 것이 많네....

    return answers[0][1] if answers else [-1]


# 하... 예제 하나가 딱 안되네... 처음에 answers에 너무 많이 들어갔다. 그 부분을 start 지점을 정해서 줄일 수 있었다.
solution(10, [0,0,0,0,0,0,0,0,3,4,3])