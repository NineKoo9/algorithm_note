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



def solution2():
    from collections import deque
    import sys

    input = sys.stdin.readline 

    N, M, K = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(N)]

    # visited[k][i][j]는 k개 부수고 i, j까지 도착하는 최단 경로
    # 시간복잡도는 최대 천만이다. 
    visited = [[[-1] * M for _ in range(N)] for _ in range(K + 1)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    q = deque()
    for i in range(K + 1):
        visited[i][0][0] = 1
    q.append((0, 0, 1, 0))
    while q:
        r, c, dist, cnt = q.popleft()
        if r == N - 1 and c == M - 1:
            # 최단거리가 될 것이다.
            print(dist)
            exit()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 먼저 경로를 벗어나면 안된다.
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 이미 방문한 적 있다면? 방문하지 않는다.
            if visited[cnt][nr][nc] != -1:
                continue

            # 만약 벽이라면
            if board[nr][nc] == 1:
                if cnt < K: # 부순 갯수가 K개 미만이면
                    visited[cnt + 1][nr][nc] = 1
                    q.append((nr, nc, dist + 1, cnt + 1))
                else: # 부술 수 있는 것이 없다면
                    continue
            # 만약 벽이 아니라면 그냥 간다.
            else:
                visited[cnt][nr][nc] = 1
                q.append((nr, nc, dist + 1, cnt))
    print(-1)


solution2()