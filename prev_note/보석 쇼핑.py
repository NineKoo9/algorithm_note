def solution(gems):
    def check(s, e):
        sub_set = set()
        for gem in gems[s:e + 1]:
            sub_set.add(gem)
        return len(gem_names - sub_set) == 0

    gem_names = set()
    for gem in gems:
        if gem in gem_names:
            continue
        gem_names.add(gem)

    answers = []
    start = 0
    end = 0
    while 0 <= start <= end < len(gems):
        if check(start, end):
            answers.append([start + 1, end + 1])
            start += 1
        else:
            end += 1
    return sorted(answers, key=lambda answer: (answer[1] - answer[0], answer[0]))[0]

# 우선 위의 코드는 시간초과가 발생하였다.

from collections import deque


def solution2(gems):
    def q_check():
        if is_zero_exist:
            return False
        # 여기서 모든 원소가 다 있는지 체크해야한다.
        for v in gem_q_count.values():
            if v == 0:
                return False
        return True

    q = deque()
    gem_q_count = {gem: 0 for gem in gems}
    is_zero_exist = True
    answers = []
    for idx, gem in enumerate(gems):
        while q_check():
            is_zero_exist = False
            answers.append([q[0][0] + 1, q[-1][0] + 1])
            prev_idx, pop_gem = q.popleft()
            gem_q_count[pop_gem] -= 1
            if gem_q_count[pop_gem] == 0:
                is_zero_exist = True
        gem_q_count[gem] += 1
        q.append((idx, gem))
    while q and q_check():
        answers.append([q[0][0] + 1, q[-1][0] + 1])
        prev_idx, pop_gem = q.popleft()
        gem_q_count[pop_gem] -= 1

    return sorted(answers, key=lambda answer: (answer[1] - answer[0], answer[0]))[0]

solution2(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])

# 2번 3번 모두 시간초과가 발생한다... 확률도 똑같다...
def solution3(gems):
    def check():
        # 여기서 모든 원소가 다 있는지 체크해야한다.
        for v in gem_count.values():
            if v == 0:
                return False
        return True

    gem_count = {gem: 0 for gem in gems}
    answers = []
    start = 0
    end = 0
    gem_count[gems[start]] += 1
    while 0 <= start <= end < len(gems):
        if check():
            answers.append((start + 1, end + 1))
            # start 부분을 제거해야지
            gem_count[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end < len(gems):
                gem_count[gems[end]] += 1

    return sorted(answers, key=lambda answer: (answer[1] - answer[0], answer[0]))[0]

# 와... 미쳤다 시간 최적화를 위해서 map의 키를 제거하다니...역시 대단해
def solution4(gems):
    def check():
        # 여기서 모든 원소가 다 있는지 체크해야한다.
        if len(gem_count) < N:
            return False
        return True

    gem_count = {}
    N = len({gem: 0 for gem in gems})
    answers = []
    start = 0
    end = 0
    gem_count[gems[start]] = 1
    while 0 <= start <= end < len(gems):
        if check():
            answers.append((start + 1, end + 1))
            gem_count[gems[start]] -= 1
            if gem_count[gems[start]] == 0:
                del gem_count[gems[start]]
            start += 1
        else:
            end += 1
            if end < len(gems):
                if gems[end] in gem_count:
                    gem_count[gems[end]] += 1
                else:
                    gem_count[gems[end]] = 1

    return sorted(answers, key=lambda answer: (answer[1] - answer[0], answer[0]))[0]
