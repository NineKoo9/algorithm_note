def solution():
    from collections import deque
    import sys

    M, N = map(int, sys.stdin.readline().split())  # M은 가로 N 은 세로 각각 1000 까지 최대 총 10만개 까지
    Box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 처음부터 익어있는 토마토의 위치를 구한다.
    tomato_positions = []
    zero_count = 0
    for i in range(N):
        for j in range(M):
            if Box[i][j] == 1:
                tomato_positions.append((i, j))
            if Box[i][j] == 0:
                zero_count += 1
    # 각 토마토의 위치들에 대해서 동시에 bfs 가 진행이 되어야 하는데...
    q = deque()
    for start_position in tomato_positions:
        q.append((start_position, 0))
    result = 0
    while q:
        current_position, count = q.popleft()
        y, x = current_position
        # 다 익었는지 체크한다. 근데... 그 체크를 매번 한다...?
        if zero_count == 0:
            result = count
            break
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if (0 <= n_x < M and 0 <= n_y < N) and (Box[n_y][n_x] == 0):
                Box[n_y][n_x] = 1
                zero_count -= 1
                q.append(((n_y, n_x), count + 1))
    # 무엇으로 끝났는지 모르니까... check 로 끝났다면 q 가 남아있을수있다. 반복문을 다 처리했다면?
    if zero_count == 0:
        if q:
            _, count = q.pop()
            result = max(result, count)
        print(result)
    else:
        print(-1)

def solution2():
    from collections import deque

    M, N = map(int, input().split())  # 가로, 세로
    tomato_box = [list(map(int, input().split())) for _ in range(N)]
    count = 0  # 단 토마토가 모두 익지 못한다면 -1이 되어야 한다.
    ripe_tomatoes = deque()
    empty_count = 0
    unripe_count = 0
    for i in range(N):
        for j in range(M):
            if tomato_box[i][j] == 1:
                ripe_tomatoes.append((i, j, 0))
            elif tomato_box[i][j] == -1:
                empty_count += 1
            else:
                unripe_count += 1

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    if len(ripe_tomatoes) == M * N - empty_count:
        return count
    else:
        while ripe_tomatoes:
            ripe_tomato = ripe_tomatoes.popleft()
            y = ripe_tomato[0]
            x = ripe_tomato[1]
            count = ripe_tomato[2]
            for i in range(4):
                n_y = y + dy[i]
                n_x = x + dx[i]
                if not (0 <= n_y < N and 0 <= n_x < M and tomato_box[n_y][n_x] == 0):
                    continue
                tomato_box[n_y][n_x] = 1
                unripe_count -= 1
                ripe_tomatoes.append((n_y, n_x, count + 1))
        return count if unripe_count == 0 else -1

def solution3():
    from collections import deque

    M, N = map(int, input().split())  # 가로, 세로
    tomato_box = [list(map(int, input().split())) for _ in range(N)]

    ripe_tomatoes = []
    for i in range(N):
        for j in range(M):
            if tomato_box[i][j] == 1:
                ripe_tomatoes.append((i, j))

    dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
    q = deque()
    for ripe_tomato in ripe_tomatoes:
        q.append((ripe_tomato, 0))

    answer_day = 0
    while q:
        tomato, day = q.popleft()
        y, x = tomato
        answer_day = max(answer_day, day)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if not (0 <= ny < N and 0 <= nx < M) or tomato_box[ny][nx] != 0:
                continue
            tomato_box[ny][nx] = 1
            q.append(((ny, nx), day + 1))
    for i in range(N):
        for j in range(M):
            if tomato_box[i][j] == 0:
                print(-1)
                exit()
    print(answer_day)

solution3()