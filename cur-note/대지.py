def solution():
    INF = int(1e9)
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    x_min, y_min = INF, INF
    x_max, y_max = -INF, -INF
    for point in points:
        x_max = max(x_max, point[0])
        y_max = max(y_max, point[1])
        x_min = min(x_min, point[0])
        y_min = min(y_min, point[1])
    x_len = x_max - x_min
    y_len = y_max - y_min
    print(x_len * y_len if len(points) > 1 else 0)

solution()