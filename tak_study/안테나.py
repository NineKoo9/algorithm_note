def solution():
    N = int(input())
    house = sorted(list(map(int, input().split())))
    answer_idx = N // 2 if N % 2 == 0 else N // 2 + 1
    print(house[answer_idx-1])

solution()