from collections import deque, defaultdict

def solution():
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    new_board = [[0] * M for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    num = 1
    num_count = defaultdict(int)

    result = [[0] * M for _ in range(N)]

    q = deque()

    for i in range(N):
        for j in range(M):
            # 벽이면 제낀다.
            if board[i][j] == "1":
                continue
            # 방문했다면? 제낀다.
            if new_board[i][j] != 0:
                continue

            # 0이다? bfs 탐색한다.
            q.append((i, j))
            new_board[i][j] = num
            count = 1
            while q:
                y, x = q.popleft()
                for k in range(4):
                    n_y = y + dy[k]
                    n_x = x + dx[k]
                    # 범위를 벗어나면 안되지
                    if not (0 <= n_y < N and 0 <= n_x < M):
                        continue
                    # 벽이면 안됨
                    if board[n_y][n_x] == "1":
                        continue
                    # 방문처리한 곳이면 안됨
                    if new_board[n_y][n_x] != 0:
                        continue
                    count += 1
                    new_board[n_y][n_x] = num
                    q.append((n_y, n_x))
            num_count[num] = count
            num += 1
    # 자 이제 board을 탐색하며... 1 주위에서 0인 녀석들의 숫자들을 합하자
    for i in range(N):
        for j in range(M):
            if board[i][j] == "0":
                continue
            # 이제 1 인 경우를 살펴보는 것이다.
            result[i][j] = 1
            s = set()
            for k in range(4):
                n_i = i + dy[k]
                n_j = j + dx[k]
                if not (0 <= n_i < N and 0 <= n_j < M):
                    continue
                if board[n_i][n_j] == "1":
                    continue
                s.add(new_board[n_i][n_j])
            for ss in s:
                result[i][j] += num_count[ss]

    for row in result:
        print("".join(map(lambda r: str(r % 10), row)))

solution()