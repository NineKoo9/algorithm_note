from collections import deque

def solution(q1, q2):
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    total = sum_q1 + sum_q2
    half_total = total // 2
    q1 = deque(q1)
    q2 = deque(q2)
    for count in range(1, 3 * len(q1) - 3):
        if sum_q1 > half_total :
            out = q1.popleft()
            q2.append(out)
            sum_q1 -= out
            sum_q2 += out
        elif sum_q1 < half_total:
            out = q2.popleft()
            q1.append(out)
            sum_q1 += out
            sum_q2 -= out
        else:
            return count - 1
    return -1

# 재밋구만... 그러나 첫번째 테스트케이스가 하나 오류뜬다. 어디서 예외처리를 못한걸까?