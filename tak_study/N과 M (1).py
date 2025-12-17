def solution():
    def recur(m):
        if m == M:
            print(*selected)
            return

        for i in range(1, N + 1):
            if visited[i]:
                continue
            selected[m] = i
            visited[i] = 1
            recur(m + 1)
            visited[i] = 0

    N, M = map(int, input().split())
    selected = [0] * M
    visited = [0] * (N + 1)
    recur(0)

solution()