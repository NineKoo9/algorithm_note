def solution():
    def dfs(y, x, count):
        visited[y][x] = 1
        count += 1
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if (0 <= n_x < N and 0 <= n_y < N) and (table[n_y][n_x] == 1) and (visited[n_y][n_x] == 0):
                count = dfs(n_y, n_x, count)
        return count

    N = int(input())
    table = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    results = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1 or table[i][j] == 0:
                continue
            results.append(dfs(i, j, 0))

    results.sort()
    print(len(results))
    print(*results, sep="\n")


solution()
# 머릿속에 드는 방법은 한점한점 dfs 을 수행하는 것인데...
# 이것을 한번에 처리하는 것이 있을까?