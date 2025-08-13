def solution():
    def recur(cur, start):
        if cur == M:
            print(*selected)
            return
        for n in range(start, N + 1):
            selected[cur] = n
            recur(cur + 1, n)

    N, M = map(int, input().split())
    selected = [0] * M
    recur(0, 1)

solution()