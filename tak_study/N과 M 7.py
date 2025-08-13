def solution():
    def recur(cur):
        if cur == M:
            print(*selected)
            return
        for i in range(N):
            n = arr[i]
            selected[cur] = n
            recur(cur + 1)

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    selected = [0] * M
    recur(0)

solution()