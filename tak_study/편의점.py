def solution():
    N = int(input())
    customers = [list(map(int, input().split())) for _ in range(N)]

    # y을 기준으로 정렬한다.
    customers.sort()
    idx = (N // 2) - 1 if N % 2 == 0 else N // 2
    y_value = customers[idx][0]

    customers.sort(key=lambda customer:customer[1])
    x_value = customers[idx][1]

    # 자 이제 각 위치로 부터 거리를 구해야겠는데?

    answer = []
    for c_y, c_x in customers:
        answer.append(abs(c_y - y_value) + abs(c_x - x_value))
    print(sum(answer))

solution()