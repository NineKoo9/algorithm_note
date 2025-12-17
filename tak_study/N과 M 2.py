def solution():
    def recur(cur, start):
        if cur == M:
            print(*selected)
            return

        for n in range(start, N + 1):
            selected[cur] = n
            recur(cur + 1, n + 1)

    N, M = map(int, input().split())
    selected = [0] * M
    visited = [0] * (N + 1)
    recur(0, 1)

solution()