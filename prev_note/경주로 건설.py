def solution2(board):
    import heapq

    dy = [-1, 1, 0, 0]  # 상하좌우가 된다.
    dx = [0, 0, -1, 1]
    N = len(board)
    costs = []
    q = []
    min_costs = [[[int(1e9)] * N for _ in range(N)] for _ in range(4)]
    for i in range(4):
        min_costs[i][0][0] = 0
        heapq.heappush(q, (0, (0, 0), i))  # 비용, 좌표, 방향
    while q:
        cost, point, d = heapq.heappop(q)
        y, x = point
        if point == (N - 1, N - 1):
            costs.append(cost)
        if min_costs[d][y][x] < cost: # 현재 내가 온 방향으로 부터 더 작은 값이 갱신된 것이 있다면 그 녀석은 건너뛴다.
            continue
        for n_d in range(4):
            n_y = y + dy[n_d]
            n_x = x + dx[n_d]
            if not (0 <= n_x < N and 0 <= n_y < N and board[n_y][n_x] == 0):
                continue
            if d != n_d:
                if min_costs[n_d][n_y][n_x] > cost + 600:
                    # 최소값이 같더라도 방향에 따라서 다음의 최소값이 달라질수있으니 등호를 추가해서 고려해주자.
                    min_costs[n_d][n_y][n_x] = cost + 600
                    heapq.heappush(q, (cost + 600, (n_y, n_x), n_d))
            else:
                if min_costs[n_d][n_y][n_x] > cost + 100:
                    min_costs[n_d][n_y][n_x] = cost + 100
                    heapq.heappush(q, (cost + 100, (n_y, n_x), n_d))

    return min(costs)



# print(solution([[0,1,0,0,0],[0,0,0,1,0],[1,1,1,0,0],[0,0,0,0,1],[0,0,0,0,0]]))

# 아... 역시 db 에서 방향을 고려해줘야하나?

import heapq


def dijkstra(start, board):
    N = len(board)
    INF = int(1e9)
    dp = [[INF] * N for _ in range(N)]

    y, x = start
    # 상 우 하 좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    h = []
    dp[y][x] = 0
    heapq.heappush(h, (0, y, x, -1))  # 여기에 값을 넣는 순서가 중요하다.
    while h:
        cost, y, x, direction = heapq.heappop(h)  # 반복문에서 i가 방향에 해당될텡데...
        print(y, x, cost, direction)
        if dp[y][x] < cost:  # 여기 등호를 왜 넣으면 안되지? 아 시작조차 안되는구나
            continue

        for next_direction in range(4):
            n_y = y + dy[next_direction]
            n_x = x + dx[next_direction]
            # 다음 지점까지의 비용을 계산한다. 홀수 짝수로 구분
            next_cost = cost + (100 if direction % 2 == next_direction % 2 else 600)
            # 첫 출발지점이라면, 다음 지점까지의 비용은 100에 해당되지.
            if (y, x) == start:
                next_cost = 100
            # board 범위 안이고, board에서 길에 해당.
            if not (0 <= n_y < N and 0 <= n_x < N and board[n_y][n_x] == 0):
                continue
            # 여기에서 굳이 방문처리 안해도 이미 왔던 길은 안가게 되지 않을까?
            if dp[n_y][n_x] >= next_cost:  # 여기서 값이 같은 경우는... 방향때문에 한번 넣어주는 것이 맞겠다.
                dp[n_y][n_x] = next_cost
                heapq.heappush(h, (dp[n_y][n_x], n_y, n_x, next_direction))
    return dp


def solution(board):
    # 최소비용이 들기 위해서는 코너가 적어야겠다?
    # 총 칸의 갯수는 625
    # 완전탐색이 이루어져야겠는데? 최대 625개의 칸에 대해서... 탐색 경우의수는.. 오른쪽으로 24번 왼쪽으로 24번...
    # 총 경우의 수는 저것들을 배치하는 방법의 수... 너무 크다. 그러면 기록을 해나가야겠네? db을 쓸까
    # 최단거리가 아니라 최소 비용이다. 특정점까지의 최소 비용은 고정값을 것이다.
    N = len(board)
    dp = dijkstra((0, 0), board)
    return dp[N - 1][N - 1]


print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [1, 1, 1, 0, 0]]))


# dp에 방향을 고려한 새로운 풀이
import heapq

def dijkstra(start, board):
    N = len(board)
    INF = int(1e9)
    dp = [[[INF] * N for _ in range(N)] for _ in range(4)]

    y, x = start
    # 상 우 하 좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    h = []
    for d in range(4):
        dp[d][y][x] = 0
    heapq.heappush(h, (0, y, x, -1))  # 여기에 값을 넣는 순서가 중요하다.
    while h:
        cost, y, x, direction = heapq.heappop(h)  # 반복문에서 i가 방향에 해당될텡데...
        if dp[direction][y][x] < cost:  # 여기 등호를 왜 넣으면 안되지? 아 시작조차 안되는구나
            continue

        for next_direction in range(4):
            n_y = y + dy[next_direction]
            n_x = x + dx[next_direction]
            # 다음 지점까지의 비용을 계산한다. 홀수 짝수로 구분
            next_cost = cost + (100 if direction % 2 == next_direction % 2 else 600)
            # 첫 출발지점이라면, 다음 지점까지의 비용은 100에 해당되지.
            if (y, x) == start:
                next_cost = 100
            # board 범위 안이고, board에서 길에 해당.
            if not (0 <= n_y < N and 0 <= n_x < N and board[n_y][n_x] == 0):
                continue
            # 여기에서 굳이 방문처리 안해도 이미 왔던 길은 안가게 되지 않을까?
            if dp[next_direction][n_y][n_x] > next_cost:  # 여기서 값이 같은 경우는... 방향때문에 한번 넣어주는 것이 맞겠다.
                dp[next_direction][n_y][n_x] = next_cost
                heapq.heappush(h, (dp[next_direction][n_y][n_x], n_y, n_x, next_direction))
    return dp


def solution(board):
    # 최소비용이 들기 위해서는 코너가 적어야겠다?
    # 총 칸의 갯수는 625
    # 완전탐색이 이루어져야겠는데? 최대 625개의 칸에 대해서... 탐색 경우의수는.. 오른쪽으로 24번 왼쪽으로 24번...
    # 총 경우의 수는 저것들을 배치하는 방법의 수... 너무 크다. 그러면 기록을 해나가야겠네? db을 쓸까
    # 최단거리가 아니라 최소 비용이다. 특정점까지의 최소 비용은 고정값을 것이다.
    N = len(board)
    dp = dijkstra((0, 0), board)
    return min(dp[d][N - 1][N - 1] for d in range(4))

# print(solution([[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 0, 1, 0, 0],[1, 0, 0, 0, 1],[1, 1, 1, 0, 0]]))
