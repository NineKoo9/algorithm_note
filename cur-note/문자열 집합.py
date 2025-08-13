def solution():
    N, M = map(int, input().split())
    s1_tmp = [input() for _ in range(N)]
    s1 = {}
    for s in s1_tmp:
        s1[s] = 1
    s2 = [input() for _ in range(M)]
    count = 0
    for s in s2:
        if s in s1:
            count += 1
    print(count)


solution()