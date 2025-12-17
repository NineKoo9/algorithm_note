def solution():
    from collections import deque

    T = int(input())
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    for _ in range(T):
        L = int(input())  # 길이는 4 ~ 300
        cur_y, cur_x = map(int, input().split())
        des_y, des_x = map(int, input().split())
        visited = [[0] * L for _ in range(L)]

        # 여기서 bfs 을 수행하자.
        q = deque()
        visited[cur_y][cur_x] = 1
        q.append((cur_y, cur_x, 0))
        while q:
            y, x, count = q.popleft()
            if y == des_y and x == des_x:
                print(count)
                break
            for i in range(8):
                n_y = y + dy[i]
                n_x = x + dx[i]
                if (0 <= n_x < L and 0 <= n_y < L) and (visited[n_y][n_x] == 0):
                    visited[n_y][n_x] = 1
                    q.append((n_y, n_x, count + 1))


solution()