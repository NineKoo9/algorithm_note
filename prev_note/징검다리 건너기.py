def solution(stones, k):
    def check(person_num, k):
        stack = []
        for stone in stones:
            diff = stone - person_num + 1
            if diff > 0:
                if len(stack) + 1 > k:
                    return False
                stack = []
            else:
                stack.append(0)
        if len(stack) + 1 > k:
            return False
        return True

    start = 0
    end = max(stones) + 2
    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid, k):
            start = mid
        else:
            end = mid
    return start

# 위의 풀이는 계속 8, 10, 12 에서 시간초과가 발생한다.
def solution2(stones, k):
    def check(person_num, k):
        jump = 0
        for stone in stones:
            diff = stone - person_num + 1
            if diff > 0:
                if jump + 1 > k:
                    return False
                jump = 0
            else:
                jump += 1
        return False if jump + 1 > k else True

    start = 2
    end = max(stones) + 2
    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid, k):
            start = mid
        else:
            end = mid
    return start


def solution3(stones, k):
    def check(m, k):  # 최대 사이 거리라 하자.
        zero = 0
        for stone in stones:  # 심지어 i로 받고 stones[i] 로 하는 것도 통과못하고...
            temp = stone - m + 1
            if temp <= 0:
                zero += 1
            else:
                if zero + 1 > k:
                    return False
                zero = 0
        return True if zero + 1 <= k else False

    # 이야... 여기서 참 최적화라니... 어마어마하네
    def check1(m, k):
        temp_stones = list(map(lambda stone: stone-m+1 if stone-m+1 >= 0 else 0, stones))
        max_continuous_zero = 0
        point = 0
        continuous_zero = 0
        while point < len(stones):
            while point < len(stones) and stones[point] == 0:
                point += 1
                continuous_zero += 1
                max_continuous_zero = max(max_continuous_zero, continuous_zero)
            point += 1
            continuous_zero = 0
        return True if max_continuous_zero + 1 <= k else False

    s = 0
    e = max(stones) + 1
    while s + 1 < e:
        mid = (s + e) // 2
        if check(mid, k):
            s = mid
        else:
            e = mid
    return s