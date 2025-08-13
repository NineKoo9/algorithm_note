def solution():
    def recur(cur):
        if cur == M:
            print(*selected)
            return
        for n in arr:
            if visited[n]:
                continue
            visited[n] = 1
            selected[cur] = n
            recur(cur + 1)
            visited[n] = 0


    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    selected = [0] * M
    visited = {n: 0 for n in arr}
    recur(0)

solution()