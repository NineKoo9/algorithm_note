from collections import deque
def solution():
    def bfs(start):
        q = deque()
        visited[start[0]][start[1]] = 1
        q.append(start)
        while q:
            y, x = q.popleft()
            for i in range(4):
                n_y = y + dy[i]
                n_x = x + dx[i]
                if 0 <= n_x < M and 0 <= n_y < N and (visited[n_y][n_x] == 0) and (graph[n_y][n_x] == 1):
                    visited[n_y][n_x] = 1
                    q.append((n_y, n_x))

    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        graph = [[0] * M for _ in range(N)]
        visited = [[0] * M for _ in range(N)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        count = 0
        for _ in range(K):
            X, Y = map(int, input().split())
            graph[Y][X] = 1
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 1 or graph[i][j] == 0:
                    continue
                bfs((i, j))
                count += 1
        print(count)

solution()