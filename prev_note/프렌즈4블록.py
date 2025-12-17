def solution(m, n, board):
    def get_remove_index(b):
        remove_index = set()
        for i in range(len(b) - 1):
            for j in range(len(b[0]) - 1):
                if b[i][j] == '0':
                    continue
                if b[i][j] == b[i+1][j] == b[i][j+1] == b[i+1][j+1]: # 여기서 심각한 문제가 발생했네... 같은 녀셕을 체크하고 있어...
                    remove_index.add((i, j))
                    remove_index.add((i+1, j))
                    remove_index.add((i, j+1))
                    remove_index.add((i+1, j+1))
        return remove_index
    
    def update(idxs):        
        for y, x in idxs:
            board[y][x] = '0'
        stack = []
        for j in range(len(board[0])):
            for i in range(len(board)):
                if board[i][j] != '0':
                    stack.append(board[i][j])
            for i in reversed(range(len(board))):
                board[i][j] = stack.pop() if stack else '0'

    board = [list(row) for row in board]
    while 1:
        remove_index = get_remove_index(board)
        if not remove_index:
            break
        update(remove_index)       
    return sum([row.count("0") for row in board])


def solution2(m, n, board):
    def get_remove_points():
        points = set()
        for i in range(n - 1):
            for j in range(m - 1):
                if new_board[i][j] == "":
                    continue
                if new_board[i][j] == new_board[i + 1][j] == new_board[i][j + 1] == new_board[i + 1][j + 1]:
                    points |= set([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])
        return points

        return new_board[i][j] == new_board[i + 1][j] == new_board[i][j + 1] == new_board[i + 1][j + 1]

    new_board = [[board[j][i] for j in reversed(range(m))] for i in range(n)]
    remove_points = set()
    count = 0
    while 1:
        remove_points = get_remove_points()
        if not remove_points:
            break
        count += len(remove_points)
        for remove_point in remove_points:
            i, j = remove_point  # 이 녀석들을 어떻게 제거하지?
            new_board[i][j] = ""
        for i in range(n):
            for j in reversed(range(m)):
                if new_board[i][j] == "":
                    new_board[i].pop(j)
                    new_board[i].append("")
    return count


def solution3(m, n, board):
    def check(board):
        indices = set()
        for i in range(len(board) - 1):
            for j in range(len(board[0]) - 1):
                if 0 != board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    indices.add((i, j))
                    indices.add((i, j + 1))
                    indices.add((i + 1, j))
                    indices.add((i + 1, j + 1))
        return indices

    def renew_board(board, indices):
        new_board = [[] for _ in range(len(board))]
        for i in range(len(board)):
            zero_count = 0
            for j in range(len(board[0])):
                if (i, j) in indices:
                    zero_count += 1
                    continue
                new_board[i].append(board[i][j])
            while zero_count != 0:
                new_board[i].append(0)
                zero_count -= 1

        return new_board

    temp_board = [[] for _ in range(n)]

    for j in range(n):
        for i in reversed(range(m)):
            temp_board[j].append(board[i][j])

    # board을 회전하여 스택에 넣었다.
    board = temp_board  # 크기는 n * m이 되었다.

    count = 0
    while 1:
        remove_indices = check(board)
        # 제거해야할 곳이 없다면...
        if not remove_indices:
            break
        count += len(remove_indices)
        board = renew_board(board, remove_indices)

    return count




