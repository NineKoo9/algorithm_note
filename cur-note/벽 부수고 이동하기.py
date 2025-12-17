# def solution():
#     from collections import deque
#
#     N, M = map(int, input().split())
#     Map = [list(map(int, list(input()))) for _ in range(N)]
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     start = (0, 0)
#     end = (N - 1, M - 1)
#     visited = [[[0] * M for _ in range(N)] for _ in range(2)]
#
#     q = deque()
#     visited[1][start[0]][start[1]] = 1
#     q.append((start, 1, 1))
#     while q:
#         cur_node, wild_card, count = q.popleft()
#         if cur_node == end:
#             print(count)
#             exit()
#         y, x = cur_node
#
#         for i in range(4):
#             n_y = y + dy[i]
#             n_x = x + dx[i]
#             if (0 <= n_x < M and 0 <= n_y < N) and (visited[wild_card][n_y][n_x] == 0) and (Map[n_y][n_x] == 0):
#                 visited[wild_card][n_y][n_x] = 1
#                 q.append(((n_y, n_x), wild_card, count + 1))
#
#         if wild_card:
#             for i in range(4):
#                 n_y = y + 2 * dy[i]
#                 n_x = x + 2 * dx[i]
#                 if (0 <= n_x < M and 0 <= n_y < N) and (visited[wild_card - 1][n_y][n_x] == 0) and (Map[n_y][n_x] == 0):
#                     visited[wild_card - 1][n_y][n_x] = 1
#                     q.append(((n_y, n_x), wild_card - 1, count + 2))
#
#     print(-1)

def solution2():
    from collections import deque

    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    end = (N - 1, M - 1)
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1  # 벽을 안뚫고 왔다? 벽을 뚫고 가장 빨리 온 지점이 있다면 그 뒤는 고려할 필요가 없지
    while q:
        y, x, broken = q.popleft()
        if (y, x) == end:
            print(visited[broken][y][x])
            exit()
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if not (0 <= n_y < N and 0 <= n_x < M and visited[broken][n_y][n_x] == 0):
                continue
            # 자 이제 행렬을 판단해보자 벽인지 아니면 길인지
            if matrix[n_y][n_x] == "1":
                if broken:
                    continue
                visited[1][n_y][n_x] = visited[broken][y][x] + 1
                q.append((n_y, n_x, 1))
            else:
                visited[broken][n_y][n_x] = visited[broken][y][x] + 1
                q.append((n_y, n_x, broken))
    print(-1)

def solution3():
    from collections import deque

    N, M = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(N)]
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    dp = {broken: [[-1] * M for _ in range(N)] for broken in [False, True]}  # 0은 벽을 부수지 않고 도착. 1은 벽을 부수고 도착. dp에서 visited을 대체해도 될 듯 하다
    start, end = (0, 0), (N - 1, M - 1)
    q = deque()
    q.append((start, 1, False))
    dp[False][0][0] = 1

    while q:
        node, dist, break_down = q.popleft()
        if node == end:
            print(dist)
            exit()

        y, x = node
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 범위를 벗어나면 건너뛴다.
            if not (0 <= ny < N and 0 <= nx < M):
                continue

            if board[ny][nx] == 0 and dp[break_down][ny][nx] == -1:
                dp[break_down][ny][nx] = dist + 1
                q.append(((ny, nx), dist + 1, break_down))

            # 예외적으로 깨부수지 않았다면.. 벽도 탐색가능하다. 그리고 기본적으로 0만 탐색 가능하다.
            elif break_down == False and board[ny][nx] == 1 and dp[True][ny][nx] == -1:
                dp[True][ny][nx] = dist + 1
                q.append(((ny, nx), dist + 1, True))
    print(-1)

solution3()