def get_dist(p1: tuple, p2: tuple):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solution():
    from itertools import combinations
    
    # 0 is empty, 1 is home, 2 is chicken store
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    home_points = []
    chick_points = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                home_points.append((i, j))
            elif board[i][j] == 2:
                chick_points.append((i, j))
    
    # 어쨋든 전체 치킨집 중에서 몇개를 선택해야한다.
    # 난 이제부터 각 집에서 모든 치킨집까지의 거리를 구할 것이다.
    dist = [[0] * len(chick_points) for _ in range(len(home_points))]
    for h_idx, home_point in enumerate(home_points):
        # 이 한점에서 모든 치킨집의 거리를 구해보자.
        for c_idx, chick_point in enumerate(chick_points):
            dist[h_idx][c_idx] = get_dist(home_point, chick_point)
    
    # 이제부터 치킨집들중에서 선택을 해야한다.
    ans = int(1e9)
    for m in range(1, M + 1):  # 사실 이 반복문은 없어도 된다. 치킨집은 M개보다 항상 크거나 같다. M개 이하로 선택한 경우를 따질필요 없이 하나하나 체크하니 최대 M개만 획득하고 거리를 구하는 것이 조금 더 그리디하게 맞다?
        for selected_chick_idices in combinations(range(len(chick_points)), m):  # 치킨집을 m개 선택했다.
            city_chicken_dist = 0
            for home_idx in range(len(home_points)):
                chick_dist = int(1e9)
                for chick_idx in selected_chick_idices:
                    chick_dist = min(chick_dist, dist[home_idx][chick_idx])
                city_chicken_dist += chick_dist
            ans = min(ans, city_chicken_dist)
    print(ans)
                
            
            

solution()