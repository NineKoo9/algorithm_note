def solution():
    from collections import deque

    N, M, K = map(int, input().split())

    table = [input() for _ in range(N)]

    start = (0, 0)
    end = (N - 1, M - 1)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]

    q = deque()
    q.append((0, 0, 1, 0))
    # 이야... 이부분...
    for i in range(K + 1):
        visited[i][0][0] = 1
    while q:
        y, x, dist, break_count = q.popleft()
        if end == (y, x):
            print(dist)
            exit()

        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            # 막다른 길이면 탐색을 못하지
            if not (0 <= n_y < N and 0 <= n_x < M):
                continue

            # 방문했던 경우라도 탐색하지 못한다.
            if visited[break_count][n_y][n_x] == 1:
                continue

            # 만약 벽이라면?
            if table[n_y][n_x] == "1":
                if break_count < K:
                    n_break_count = break_count + 1
                    visited[n_break_count][n_y][n_x] = 1
                    q.append((n_y, n_x, dist + 1, n_break_count))
                else: # 더이상 부술수도 없다면 탐색을 끝낸다.
                    continue
            else:
                visited[break_count][n_y][n_x] = 1
                q.append((n_y, n_x, dist + 1, break_count))
    print(-1)

solution()