def solution():
    def recur(cur, start):
        if cur == M:
            print(*selected)
            return

        for i in range(start, N):
            n = arr[i]
            selected[cur] = n
            recur(cur + 1, i + 1)

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    selected = [0] * M
    recur(0, 0)

solution()