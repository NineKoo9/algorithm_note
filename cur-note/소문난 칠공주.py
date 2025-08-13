from itertools import combinations

def solution():
    def check(c):
        points = []
        s_count = 0
        y_count = 0
        for num in c:
            i, j = board_point[num]
            ch = board[i][j]
            if ch == "S":
                s_count += 1
            else:
                y_count += 1
            points.append((i, j))
        if s_count < 4:
            return False

        l = [points.pop()]
        while l:
            y, x = l.pop()
            for i in range(4):
                n_y = y + dy[i]
                n_x = x + dx[i]
                if (n_y, n_x) in points:
                    l.append((n_y, n_x))
                    points.remove((n_y, n_x))
        return True if len(points) == 0 else False


    board = [input() for _ in range(5)]
    board_point = {}

    num = 0
    for i in range(5):
        for j in range(5):
            board_point[num] = (i, j)
            num += 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    count = 0
    for comb in combinations([i for i in range(25)], 7):
        if check(comb):
            count += 1

    print(count)


solution()