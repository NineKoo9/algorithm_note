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


def solution2():
    from collections import defaultdict, deque
    import sys

    sys.setrecursionlimit(10000)

    def bfs(y, x, group_idx):
        q = deque()
        q.append((y, x))
        find_group_idx[y][x] = group_idx
        size_of_groups[group_idx] += 1
        while q:
            y, x = q.popleft()

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if not (0<= ny < N and 0 <= nx < M):
                    continue
                if find_group_idx[ny][nx] != -1 or board[ny][nx] == 1:
                    continue
                find_group_idx[ny][nx] = group_idx
                size_of_groups[group_idx] += 1
                q.append((ny, nx))

    # 만약 벽 하나에 모두 빈칸이라면 최대 10만개까지 갈지도..
    def dfs(y, x, count, group_idx):
        find_group_idx[y][x] = group_idx
        size_of_groups[group_idx] += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not (0<= ny < N and 0 <= nx < M):
                continue
            if find_group_idx[ny][nx] != -1 or board[ny][nx] == 1:
                continue
            dfs(ny, nx, count + 1, group_idx)

    N, M = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(N)]
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    # 모든 벽에 대해서 그 벽을 부수고 그 위치에서 이동할 수 있는 칸의 수를 모두 세어야한다.
    # 벽이 10만개이고 벽이 한 만개 있다 해보자. 
    wall_points = []
    answer = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                wall_points.append((i, j))

    # 포인트들이 어떤 그룹에 속하는지 알아야하고
    # 그룹안에 어떤 포인트들이 속해 있는지 알아야한다.
    size_of_groups = defaultdict(int)
    find_group_idx = [[-1] * M for _ in range(N)]
    group_idx = 0
    for i in range(N):
        for j in range(M):
            # 벽이거나 이미 탐색이 끝났다면 continue
            if board[i][j] == 1 or find_group_idx[i][j] != -1:
                continue
            bfs(i, j, group_idx)
            group_idx += 1

    # 자 이제 벽들을 탐색하면서 인접한 그룹들을 탐색해서 총 몇개가 필요한지 찾아본다 단 그룹이 중복되면 안된다.
    for wall_point in wall_points:
        y, x = wall_point
        group_idx_set = set()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not (0 <= ny < N and 0 <= nx < M) or board[ny][nx] == 1:
                continue
            group_idx_set.add(find_group_idx[ny][nx])
        # 이제 인접한 그룹을 찾았으니 몇개를 움직일 수 있는지 체크한다.
        point_count = 1 + sum([size_of_groups[g_idx] for g_idx in group_idx_set])
        answer[y][x] = point_count % 10
    for row in answer:
        print("".join(list(map(str, row))))

solution2()