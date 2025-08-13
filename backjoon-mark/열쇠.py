import sys

sys.setrecursionlimit(100000)


def reset_visited():
    for i in range(h):
        for j in range(w):
            visited[i][j] = 0


def dfs(y, x):
    global count
    if board[y][x] == "$":
        count += 1
        reset_visited()
        board[y][x] = "."

    if board[y][x].islower():
        current_keys.add(board[y][x])
        reset_visited()
        board[y][x] = "."

    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        # 범위를 벗어나는 경우 탐색하지 않는다.
        if not (0 <= ny < h and 0 <= nx < w):
            continue
        # 방문을 한 경우 또는 벽인 경우 탐색하지 않는다.
        if visited[ny][nx] or board[ny][nx] == "*":
            continue
        # 자 이제 문인경우인데...
        if board[ny][nx].isupper() and board[ny][nx].lower() not in current_keys:
            continue
        dfs(ny, nx)


# dfs로 시간초과걸리는거 bfs로 풀었더니 엄청 빠르네...?
def bfs(y, x):
    from collections import deque

    global count

    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    while q:
        cur_y, cur_x = q.popleft()

        if board[cur_y][cur_x] == "$":
            count += 1
            reset_visited()
            visited[cur_y][cur_x] = 1
            q.clear()
            board[cur_y][cur_x] = "."

        if board[cur_y][cur_x].islower():
            current_keys.add(board[cur_y][cur_x])
            reset_visited()
            visited[cur_y][cur_x] = 1
            q.clear()
            board[cur_y][cur_x] = "."

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            # 범위를 벗어나는 경우 탐색하지 않는다.
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            # 방문을 한 경우 또는 벽인 경우 탐색하지 않는다.
            if visited[ny][nx] or board[ny][nx] == "*":
                continue
            # 자 이제 문인경우인데...
            if board[ny][nx].isupper() and board[ny][nx].lower() not in current_keys:
                continue
            visited[ny][nx] = 1
            q.append((ny, nx))

def expand_board(cur_board):
    # 확장을 어케하지?
    new_h = len(cur_board) + 2
    new_w = len(cur_board[0]) + 2
    new_board = [["."] * new_w for _ in range(new_h)]
    for i in range(len(cur_board)):
        for j in range(len(cur_board[0])):
            new_board[i + 1][j + 1] = cur_board[i][j]
    return new_board



T = int(input())
for _ in range(T):
    count = 0
    h, _ = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    current_keys = set(input())

    board = expand_board(board)
    h, w = len(board), len(board[0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 열쇠를 획득하면 방문기록을 초기화하는 것도 괜찮을 듯한다.
    visited = [[0] * w for _ in range(h)]
    # 0 ,0 에서 탐색을 시작한다.
    bfs(0, 0)
    # 만약에 획득하러 들어갔다가 다시 뒤돌아 나오는 경우는 어케해야하노...?
    print(count)