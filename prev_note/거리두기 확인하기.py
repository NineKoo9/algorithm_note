from collections import deque

def solution(places):
    def check(p):
        # 흠... bfs 또는 dfs 을 사용하는 것 같은데...
        # 최단거리가 2이하면 안된다.
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        human_points = []
        for i in range(5):
            for j in range(5):
                if p[i][j] == "P":
                    human_points.append((i, j))
        for human_point in human_points:
            # 각 포인트에서 bfs 을 실행한다.
            q = deque()
            visited = [[0] * 5 for _ in range(5)]
            q.append((human_point, 0))
            visited[human_point[0]][human_point[1]] = 1
            while q:
                point, dist = q.popleft()
                y, x = point
                if dist >= 2:
                    break
                for i in range(4):
                    n_y = y + dy[i]
                    n_x = x + dx[i]
                    if not (0 <= n_y < 5 and 0 <= n_x < 5 and p[n_y][n_x] != "X" and visited[n_y][n_x] == 0):
                        continue
                    if p[n_y][n_x] == "P":
                        return 0
                    visited[n_y][n_x] = 1
                    q.append(((n_y, n_x), dist + 1))
        return 1

    answer = []
    for place in places:
        answer.append(check(place))
    return answer


# 다시 풀어본 풀이
from collections import deque


def bfs(person, place):
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    init_y, init_x = person
    visited = [[0] * 5 for _ in range(5)]
    visited[init_y][init_x] = 1
    q = deque()
    q.append((init_y, init_x, 0))
    while q:
        y, x, dist = q.popleft()
        if dist > 2:  # dist가 3까지 왔다면 2이하에 걸린 녀석이 없다는 뜻
            break
        if y != init_y and x != init_x and place[y][x] == "P":  # 이 조건은 잘못된 조건이다... 내가 원하는 것은 처음위치와 다른 것인데.. 이 경우 (0, 0) (2, 0)도 조건에 만족이되어 False가 반환된다...
            return False  # 이 place는 거리두기 안됨.
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if not (0 <= n_y < 5 and 0 <= n_x < 5 and place[n_y][n_x] != "X" and visited[n_y][n_x] == 0):
                continue
            visited[n_y][n_x] = 1
            q.append((n_y, n_x, dist + 1))
    return True


def check(place):
    persons = []
    for i, row in enumerate(place):
        for j, desk in enumerate(row):
            if desk == "P":
                persons.append((i, j))

    for person in persons:
        if not bfs(person, place):
            return 0
    return 1


def solution(places):
    # 각 대기실이 거리두기를 지키고 있으면 1반환
    # 한 명이라도 지키지 않으면 0을 반환
    result = []
    for place in places:
        result.append(check(place))
    return result
