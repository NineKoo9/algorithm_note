def solution():
    from collections import deque

    N, M = map(int, input().split())
    ladder_points = [tuple(map(int, input().split())) for _ in range(N)]
    snake_points = [tuple(map(int, input().split())) for _ in range(M)]  # 각각 최대 15

    # 저녀석들로 그래프를 만들어 가기위함인데
    ladder_dict = {}
    snake_dict = {}
    for start, end in ladder_points:
        ladder_dict[start] = end
    for start, end in snake_points:
        snake_dict[start] = end
    visited = {i: 0 for i in range(1, 101)}
    # 자 여기서 1번 칸부터 시작해서... 100 번까지 가는 것이 목표이다. 최단거리로 갈려면 "주사위" 를 몇번 돌려야 할까?
    # 결국 완전탐색으로 가야하는 것이 아닌가?
    q = deque()
    q.append((1, 0))
    while q:
        cur_point, cur_count = q.popleft()
        #  뱀이 있는 곳은 최대한 피하는 것이 맞을까? 주사위 횟수를 1 ~ 6 중에 갈수있는 거잖아. 흠... 알수가 없다 혹시 모르는 것이니까
        if cur_point in ladder_dict:
            cur_point = ladder_dict[cur_point]
        if cur_point in snake_dict:  # 이것이 겹치지는 않을 것이란 것은 문제에 주어져있다.
            cur_point = snake_dict[cur_point]

        # 목표지점에 도착했다면?
        if cur_point == 100:
            print(cur_count)
            break

        for i in range(1, 7):
            n_point = cur_point + i
            if 0 <= n_point <= 100 and (visited[n_point] == 0):
                visited[n_point] = 1
                q.append((n_point, cur_count + 1))


solution()