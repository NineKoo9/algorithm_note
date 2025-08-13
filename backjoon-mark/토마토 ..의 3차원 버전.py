def solution():
    from collections import deque

    M, N, H = map(int, input().split())
    Box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]  # M은 가로 N 은 세로
    dx = [0, 0, 1, -1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    ripe_tomatoes = []
    unripe_tomato_count = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if Box[h][n][m] == 1:
                    ripe_tomatoes.append((h, n, m))
                if Box[h][n][m] == 0:
                    unripe_tomato_count += 1

    q = deque()
    count = 0
    for t in ripe_tomatoes:
        q.append((t, 0))
    while q:
        tomato, cur_count = q.popleft()
        z, y, x = tomato
        if unripe_tomato_count == 0:
            _, last_count = q.pop() if q else (0, 0)
            count = max(cur_count, last_count)
            break
        for i in range(6):
            n_y = y + dy[i]
            n_x = x + dx[i]
            n_z = z + dz[i]
            if 0 <= n_z < H and 0 <= n_y < N and 0 <= n_x < M and (Box[n_z][n_y][n_x] == 0):
                Box[n_z][n_y][n_x] = 1
                unripe_tomato_count -= 1
                q.append(((n_z, n_y, n_x), cur_count + 1))

    if unripe_tomato_count != 0:
        print(-1)
    else:
        print(count)


solution()