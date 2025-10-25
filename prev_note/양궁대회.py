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

# 이것은 재미나이 풀이...
def solution(n, apeach_info):
    # 가장 점수 차가 큰 경우의 라이언 기록과, 그 때의 점수 차를 저장
    answer = [-1]
    max_diff = -1

    # DFS 함수 정의
    # idx: 현재 과녁 점수 (0~10), arrows_left: 남은 화살 수, lion_info: 현재까지 라이언의 기록
    def dfs(idx, arrows_left, lion_info):
        nonlocal max_diff, answer

        # 1. 재귀 종료 조건 (모든 과녁 확인 완료)
        if idx == 11:
            # 남은 화살은 모두 0점 과녁에 사용
            lion_info[10] += arrows_left
            
            # 2. 점수 계산
            lion_score, apeach_score = 0, 0
            for i in range(11):
                if lion_info[i] == 0 and apeach_info[i] == 0:
                    continue
                if lion_info[i] > apeach_info[i]:
                    lion_score += (10 - i)
                else:
                    apeach_score += (10 - i)
            
            # 3. 최고 기록 갱신
            diff = lion_score - apeach_score
            if diff > 0 and diff >= max_diff:
                # 점수 차가 같을 경우, 낮은 점수를 더 많이 맞힌 기록으로 갱신
                # (reversed(lion_info) > reversed(answer)) 트릭으로 간단히 비교 가능
                if diff > max_diff:
                    max_diff = diff
                    answer = lion_info[:]
                else: # diff == max_diff
                    # list를 뒤집어서 비교하면 낮은 점수부터 비교하는 효과
                    if list(reversed(lion_info)) > list(reversed(answer)):
                        answer = lion_info[:]

            # 백트래킹: 0점에 추가했던 화살 원상 복구
            lion_info[10] -= arrows_left
            return

        # 재귀 호출 로직
        # 경우 1: 라이언이 현재 과녁(idx)을 이기는 경우
        arrows_to_win = apeach_info[idx] + 1
        if arrows_left >= arrows_to_win:
            lion_info[idx] = arrows_to_win
            dfs(idx + 1, arrows_left - arrows_to_win, lion_info)
            lion_info[idx] = 0  # 백트래킹: 상태 원상 복구

        # 경우 2: 라이언이 현재 과녁(idx)을 지는 경우 (0발 쏘기)
        dfs(idx + 1, arrows_left, lion_info)

    # 초기 호출
    dfs(0, n, [0] * 11)
    
    return answer