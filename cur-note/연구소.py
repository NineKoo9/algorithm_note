def solution():
    from itertools import combinations
    from collections import deque

    def virus_expand():
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        q = deque(virus_points)
        visited = [[0] * M for _ in range(N)]
        # 기존의 바이러스 위치는 방문처리를 한다.
        for virus_point in virus_points:
            visited[virus_point[0]][virus_point[1]] = 1
        virus_count = len(q)
        while q:
            y, x = q.popleft()
            for i in range(4):
                n_y = y + dy[i]
                n_x = x + dx[i]
                if not (0 <= n_y < N and 0 <= n_x < M):  # 에휴... 여기서 N, M 위치를 헷갈렸네...
                    continue
                if visited[n_y][n_x] == 1:
                    continue
                if board[n_y][n_x] != 0:
                    continue
                visited[n_y][n_x] = 1
                virus_count += 1
                q.append((n_y, n_x))
        return virus_count

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    wall_count = 0
    virus_points, empty_points = [], []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                empty_points.append((i, j))
            elif board[i][j] == 1:
                wall_count += 1
            elif board[i][j] == 2:
                virus_points.append((i, j))

    max_safe_size = 0
    # 이제 빈공간에서 임의로 3개를 골라야한다.
    three_wall_points = list(combinations(empty_points, 3))
    for a, b, c in three_wall_points:
        # 위의 지점을 벽으로 만든다.
        board[a[0]][a[1]], board[b[0]][b[1]], board[c[0]][c[1]] = 1, 1, 1

        # 그리고 이 상태에서 virus가 퍼지도록 한다.
        new_virus_count = virus_expand()
        # 마지막으로 전체의 갯수에서 최대값을 구한다.
        max_safe_size = max(max_safe_size, N * M - new_virus_count - (wall_count + 3))
        # 다시 벽을 원래모습으로 되돌린다.
        board[a[0]][a[1]], board[b[0]][b[1]], board[c[0]][c[1]] = 0, 0, 0

    print(max_safe_size)

solution()