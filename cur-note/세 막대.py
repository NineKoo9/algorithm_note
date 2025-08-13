def solution():
    sticks = list(map(int, input().split()))
    sticks.sort()
    if sticks[0] + sticks[1] <= sticks[2]:
        sticks[2] = sticks[0] + sticks[1] - 1
    print(sum(sticks))


solution()