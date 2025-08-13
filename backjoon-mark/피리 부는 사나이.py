def solution():
    def is_cycle2(y, x): # 흠... 탐색을 하다가 끊길수도 있다고?
        if (y, x) in traced:
            return True
        if visited[y][x]:  # 호출스택에는 없지만 방문한 적 있는 녀석이라면... 기존의 세이프존에 포함될 녀석이군
            return False

        traced.add((y, x))
        visited[y][x] = 1
        dy, dx = directions[board[y][x]]
        n_y = y + dy
        n_x = x + dx
        if is_cycle(n_y, n_x):
            traced.remove((y, x)) # 이게 중복되는 것이 뭔가 마음에 안드는데...
            return True
        traced.remove((y, x))
        return False

    def is_cycle(y, x): # 흠... 탐색을 하다가 끊길수도 있다고?
        if (y, x) in traced:
            return True
        if visited[y][x]:  # 호출스택에는 없지만 방문한 적 있는 녀석이라면... 기존의 세이프존에 포함될 녀석이군
            return False

        traced.add((y, x))
        visited[y][x] = 1
        dy, dx = directions[board[y][x]]
        n_y = y + dy
        n_x = x + dx
        result = is_cycle(n_y, n_x)
        traced.remove((y, x))
        return result

    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    # 문제를 파악해보니 순환하는 집합이 몇개인지 판단하면 되겠다.
    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    safe_zone_count = 0
    visited = [[0] * M for _ in range(N)]
    traced = set()
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            # 탐색한 적이 없다면 사이클에 해당하는지 체크한다.
            # 사실상 방문한 적이 없다면... 특정 i번째 사이클에 무조건 포함되어 있을 것이긴 하다. 모든 점들이 사이클에 포함되어 있을테니
            # 아니다... 방문한 적이 없고 사이클을 이루지 않으며 기존의 사이클을 이루는 곳에 접근한다면... 그 녀석은 사이클 안의 세이프존에 포함되니까 가운트를 업 시킬 필요는 없다.
            if is_cycle(i, j):
                safe_zone_count += 1

    print(safe_zone_count)

solution()