def solution():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    points.sort(key=lambda point:(point[1], point[0]))
    for point in points:
        print(" ".join(map(str, point)))

solution()