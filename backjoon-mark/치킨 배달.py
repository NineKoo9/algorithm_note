from collections import deque
from itertools import combinations

def solution():
    def calc_dist(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def get_nearest_dist(house):
        # 모든 치킨 포인트에 대해서 거리를 구하면 되지 않겠나?
        # 각 점들에 대해서 모두 거리를 구할까?
        nearest_dist = int(1e9)
        for chicken in chicken_points:
            dist = calc_dist(house, chicken)
            nearest_dist = min(nearest_dist, dist)
        return nearest_dist

    def get_chicken_distance():
        all_dist = []
        for house in house_points:
            dist = get_nearest_dist(house)
            all_dist.append(dist)
        return sum(all_dist)

    N, M = map(int, input().split())
    city_board = [list(map(int, input().split())) for _ in range(N)]

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    house_points = []
    chicken_points = []
    for i in range(N):
        for j in range(N):
            if city_board[i][j] == 1:
                house_points.append((i, j))
            elif city_board[i][j] == 2:
                chicken_points.append((i, j))

    if len(chicken_points) <= M:
        dist = get_chicken_distance()
        print(dist)
    else:
        # 여기서 몇개의 치킨집을 제거해야한다.
        # 그렇다면 무엇을 제거하지?
        # 조합을 사용해야할까?
        min_dist = int(1e9)
        for c in combinations(chicken_points, M):
            chicken_points = c
            dist = get_chicken_distance()
            min_dist = min(min_dist, dist)
        print(min_dist)


solution()