def check(stones, available_number, max_jump):
    continuous_count = 0
    for stone in stones:
        continuous_count += 1
        if stone >= available_number:
            continuous_count = 0
        # continuous_count는 available_number미만의 연속된 돌의 수
        if continuous_count == max_jump:
            return False
    return True


def solution(stones, k):
    start = 0
    end = 2e8
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if check(stones, mid, k):  # mid의 갯수만큼 건널 수 있다면? 그 아래도 건널 수 있다.
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans

