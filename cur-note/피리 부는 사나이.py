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


def solution2():
    def dfs_cycle_check(y, x):
        nonlocal cycle_count
        # 만약 방문했는데 현재의 path내에 있는 녀석이라면? 사이클을 이룬다. 그렇다면 사이클을 체크하고, 탐색을 종료해도 된다.
        if (y, x) in path:
            cycle_count += 1
            return
        if visited[y][x]:
            return
        path.add((y, x))
        visited[y][x] = True
        
        dy, dx = directions[board_info[y][x]]
        n_y, n_x = y + dy, x + dx
        dfs_cycle_check(n_y, n_x)
    
    N, M = map(int, input().split())
    board_info = [list(input()) for _ in range(N)]
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    
    # 자세히 보니까... 사이클의 갯수를 확인하면 될 것 같은 느낌이다.
    # 그것으로 충분한가? 만약 사이클에 포함되지 않는 것이라면... 어떤 점들이 그냥 사이클에 일방적으로 연결되어 있다면 결국 사이클에 합류한다 그러면? 사이클에 역시 한 곳만 두면 되는 것이다.
    
    cycle_count = 0
    visited = [[False] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            # 여기서 dfs로 탐색하면서 사이클을 체크할 필요가 있다.
            path = set()
            dfs_cycle_check(i, j)
    
    safe_zone_count = cycle_count
    print(safe_zone_count)

solution2()