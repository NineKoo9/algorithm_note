def solution():
    N, M = map(int, input().split())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # bfs 시작
    from collections import deque
    q = deque()
    visited[0][0] = 1
    q.append(((0, 0), 1))
    while q:
        current_node, count = q.popleft()
        y, x = current_node
        if current_node == (N - 1, M - 1):
            print(count)
            break
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if (0 <= n_x < M and 0 <= n_y < N) and (maze[n_y][n_x] == 1) and visited[n_y][n_x] == 0:
                visited[n_y][n_x] = 1
                q.append(((n_y, n_x), count + 1))

solution()