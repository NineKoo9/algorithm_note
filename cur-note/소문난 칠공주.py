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

def solution2():
    from collections import deque
    from itertools import combinations

    def check(points: list[tuple]):
        # case안에 7개의 좌표 노드들이 들어가있다.
        # 이것을 빠르게 확인할 수 없을까? 
        s_count, y_count = 0, 0
        dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

        visited = {point: 0 for point in points}

        # 아무곳에서 시작해도 모든 점을 다 탐색할 수 있으면 OK다
        q = deque()
        visited[points[0]] = 1
        q.append(points[0])
        while q:
            curr_y, curr_x = q.popleft()

            if board[curr_y][curr_x] == "Y":
                y_count += 1
            else:
                s_count += 1

            # 탐색하는 도중에 임도연파가 4명 이상이라면 무조건 틀림
            if y_count > 3:
                return False

            for i in range(4):
                nxt_y = dy[i] + curr_y
                nxt_x = dx[i] + curr_x

                # 인접하지 않다면(포인트에 해당안되면) 제외한다.
                if (nxt_y, nxt_x) not in visited:
                    continue

                if visited[(nxt_y, nxt_x)]:
                    continue

                visited[(nxt_y, nxt_x)] = 1
                q.append((nxt_y, nxt_x))
        if y_count + s_count != 7:
            return False
        else:
            return True



    board = [input() for _ in range(5)]
    count = 0
    for points in combinations([(i, j) for j in range(5) for i in range(5)], 7):
        if check(points):
            count += 1
    print(count)


solution2()