from collections import deque

max_dist = 0
def solution():
    global max_dist
    def dfs(y, x, d):
        global max_dist
        # 종료조건...? 더이상 방문할 수 없다면 끝내야지

        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]

            if not (0 <= n_y < M and 0 <= n_x < N):
                continue
            if visited[board[n_y][n_x]] == 1:
                continue
            visited[board[n_y][n_x]] = 1
            dfs(n_y, n_x, d + 1)
            visited[board[n_y][n_x]] = 0

        max_dist = max(max_dist, d)

    M, N = map(int, input().split())
    board = [input() for _ in range(M)]

    nodes = []
    for row in board:
        for ch in row:
            nodes.append(ch)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = {a: 0 for a in nodes}
    visited[board[0][0]] = 1
    dfs(0, 0, 1)

    print(max_dist)

answer = 0
def solution2():
    from string import ascii_letters

    global answer

    def dfs(r, c, l):
        global answer

        answer = max(answer, l)
        

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            # 범위를 벗어난 경우
            if not (0 <= nr < R and 0 <= nc < C):
                continue

            # 방문했던 알파벳은 제외한다.
            value = board[nr][nc]
            if visited[value]:
                continue

            visited[value] = 1
            dfs(nr, nc, l + 1)
            visited[value] = 0



    # 최대 몇 칸을 지나는지 알고자 한다.
    R, C = map(int, input().split())
    board = [input() for _ in range(R)]

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    visited = {ch: 0 for ch in ascii_letters}
    start_value = board[0][0]
    visited[start_value] = 1
    dfs(0, 0, 1)
    print(answer)

solution2()