import copy


def combine_row(cur_row): # 하 밀기가 잘못되었구나...
    new_row = []

    # 0을 제외하고 모두 밀어버린다.
    removed_zero_row = []
    for i in range(N):
        if cur_row[i] != 0:
            removed_zero_row.append(cur_row[i])

    # 이제 같은 녀석들은 합해버린다.
    i = 0
    while 0 <= i < len(removed_zero_row):
        if i + 1 < len(removed_zero_row) and removed_zero_row[i] == removed_zero_row[i + 1]:
            value = removed_zero_row[i] * 2
            new_row.append(value)
            i += 2
        else:
            value = removed_zero_row[i]
            new_row.append(value)
            i += 1

    # 빈칸은 0으로 채워준다.
    while len(new_row) != N:
        new_row.append(0)
    return new_row

def move(cur_board, direction):
    # 우 좌 하 상
    next_board = [[0] * N for _ in range(N)]
    if direction == 0:
        for i in range(N):
            next_row = combine_row(cur_board[i][::-1])
            next_board[i] = next_row[::-1]
    elif direction == 1:
        for i in range(N):
            next_row = combine_row(cur_board[i])
            next_board[i] = next_row
    elif direction == 2:
        for i in range(N):
            next_row = combine_row([cur_board[j][i] for j in reversed(range(N))])
            next_row = next_row[::-1]
            for j in range(N):
                next_board[j][i] = next_row[j]
    else:
        for i in range(N):
            next_row = combine_row([cur_board[j][i] for j in range(N)])
            for j in range(N):
                next_board[j][i] = next_row[j]
    return next_board


def dfs(cur_board, direction, depth):
    global max_num
    if depth == 5:
        for i in range(N):
            for j in range(N):
                max_num = max(max_num, cur_board[i][j])
        return
    moved_board = move(cur_board, direction)

    for d in range(4):
        dfs(moved_board, d, depth + 1)


N = int(input())  # 보드의 크기
board = [list(map(int, input().split())) for _ in range(N)]

# 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_num = 0

for d in range(4):
    dfs(copy.deepcopy(board), d, 0)

print(max_num)
