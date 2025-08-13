def solution():
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    sum_table = [[0] * N for _ in range(N)]
    # 먼저 가로로 누적합을 수행하자
    for y in range(N):
        for x in range(N):
            sum_table[y][x] = (sum_table[y][x-1] if x-1 >= 0 else 0) + table[y][x]
    # 이번엔 새로로 누적합을 수행하자
    for y in range(N):
        for x in range(N):
            sum_table[y][x] = (sum_table[y-1][x] if y-1 >= 0 else 0) + sum_table[y][x]
        
    sum_points = [tuple(map(lambda s:int(s) - 1, input().split())) for _ in range(M)]
    for y1, x1, y2, x2 in sum_points: # 이 녀석은 최대 10만이다.
        # 여기서 저 위의 좌표에 해당하는 값들의 합을 출력한다.
        dx = x2 - x1 + 1
        dy = y2 - y1 + 1
        print(sum_table[y2][x2] - (sum_table[y2][x2 - dx] if x2 - dx >= 0 else 0) \
                                - (sum_table[y2 - dy][x2] if y2 - dy >= 0 else 0) \
                                + (sum_table[y2 - dy][x2 - dx] if y2 - dy >= 0 and x2 - dx >= 0 else 0))

solution()