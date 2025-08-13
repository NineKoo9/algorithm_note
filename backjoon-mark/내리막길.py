def solution():
    def dfs(y, x):
        # 목표지점에 도착하면 끝?
        # 외판원 순회 문제이서 힌트를 얻자... 거쳐온 녀석들이 같다면?
        if y == M - 1 and x == N - 1:
            # 여기서 값을 설정하고 되돌아갈 필요가 있을까? 그냥 끝이니까 되돌아가면 될듯?
            return 1

        # 또 어떤 경우에 끝내야할까? 이미 방문했던 지점 즉 dp값이 있는 경우?
        if dp[y][x] >= 0: # 처음에 0 초과로 설정해서 잘못되었네... 0인 경우도 체크해야지
            return dp[y][x]  # 여기서 그냥 1로 반환했더니 틀렸다. 다음 노드에서 기대되는 값이 현재 노드에 전달되어야지?

        results = [0, 0, 0, 0]
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if not (0 <= n_y < M and 0 <= n_x < N):
                continue
            if Map[y][x] > Map[n_y][n_x]:
                results[i] = dfs(n_y, n_x)
        # results에 각 방향으로의 예상 값이 적혀있을 것이다.
        dp[y][x] = sum(results)
        return dp[y][x]

    M, N = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(M)]
    dp = [[-1] * N for _ in range(M)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    dp[0][0] = dfs(0, 0)
    print(dp[0][0])

def solution2():
    import sys
    sys.setrecursionlimit(10000)

    def dfs(point):  # 하나 계속 걸리는게... 마지막지점은 무엇으로 체크하지?
        if point == end:
            return 1
        y = point[0]
        x = point[1]
        # 이미 탐색한 적이 있다면 그 위치에서 목적지까지 갈수있는 길의 수를 반환한다.
        if dp[y][x] != -1:
            return dp[y][x]
        # 이제 방문처리
        dp[y][x] = 0
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if not (0 <= n_y < M and 0 <= n_x < N and MAP[n_y][n_x] < MAP[y][x]):  # 여기서 방문을 체크하기보단... 탐색한다음 체크하자
                continue
            # 각 길에 대해서 탐색하고 갈 수 있는 길의 수를 더한다.
            dp[y][x] += dfs((n_y, n_x))
        return dp[y][x]

    M, N = map(int, sys.stdin.readline().split())  # 세로, 가로
    MAP = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
    dp = [[-1] * N for _ in range(M)]  # -1이면 아직 처리안함. 0이면 길이없는 것.
    start = (0, 0)
    end = (M - 1, N - 1)
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    # 확실히... 중복되는 연산이 존재하는데... 그 값들을 모두 업데이트한다..?
    dfs(start)
    print(dp[0][0])


def solution3():
    import sys
    sys.setrecursionlimit(10000)

    def dfs(y, x):
        # 목적지에 도착했다면 카운팅한다
        if (y, x) == (N - 1, M - 1):
            dp[y][x] = 1
            return dp[y][x]  # 사실상 1이 반환되겠지만

        # 또는 이미 방문해서 결과를 아는 지점에 대해서 그 결과를 반환한다.
        # 갈 수 있는 길의 갯수는 몇개인지 저장한다.
        if dp[y][x] != -1:
            return dp[y][x]

        dfs_result = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 우선 범위를 벗어나거나... 방문한 녀석이라면 탐색하지 않는다. 그리고 내리막길이 아니면 탐색하지 않는다.
            if not (0 <= ny < N and 0 <= nx < M) or visited[ny][nx] == 1 or board[y][x] <= board[ny][nx]:
                continue
            visited[ny][nx] = 1
            # 만약 여기서 한 방향이라도 목적지까지 도착한다면... 여기 이 노드에선 반드시 목적지까지 도착할 여지가 있다는 것이다.
            dfs_result += dfs(ny, nx)  # or 연산을 통해서 True가 하나라도 있다면 무조건 True로 만든다.
            visited[ny][nx] = 0

        dp[y][x] = dfs_result
        # 만약 더이상 갈 곳이 없다면?
        return dfs_result

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

    visited = [[0] * M for _ in range(N)]
    dp = [[-1] * M for _ in range(N)]  # 이 값은 목적지 까지 도착할 수 있는 길의 갯수를 표현한다.
    print(dfs(0, 0))

solution3()