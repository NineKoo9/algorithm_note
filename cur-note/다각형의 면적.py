def solution():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    # 여기서부터 외적을 구한다.
    answer = 0
    points.append(points[0])
    for i in range(N):
        answer += (points[i][0] * points[i + 1][1]) - (points[i + 1][0] * points[i][1])
    answer = round(abs(answer) / 2, 1)
    print(answer)

solution()