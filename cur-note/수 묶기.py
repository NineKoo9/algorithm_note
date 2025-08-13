from collections import deque

def solution():
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    minus_nums = []
    plus_nums = []
    for number in numbers:
        if number <= 0:
            minus_nums.append(number)
        elif number > 0:
            plus_nums.append(number)

    minus_nums.sort(reverse=True)
    plus_nums.sort()

    result = 0

    while len(minus_nums) > 1:
        prev = minus_nums.pop()
        cur = minus_nums.pop()
        if cur == 0:
            continue
        result += prev * cur
    if minus_nums:
        if minus_nums[0] < 0:
            result += minus_nums[0]

    while len(plus_nums) > 1:
        prev = plus_nums.pop()
        cur = plus_nums.pop()
        if cur == 1:
            result += (prev + cur)
            continue
        result += prev * cur
    if plus_nums:
        result += plus_nums[0]

    print(result)

solution()