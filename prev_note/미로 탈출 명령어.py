from collections import deque
import sys

sys.setrecursionlimit(5000)


def solution(n, m, x, y, r, c, k):
    # 가지치기를 어떻게 할 것이냐가 문제네? 겹치는게 있나? 이야... 가지치기를 이렇게 했어야했네....
    # 하... 겹치는 분야가 어딘지 제대로 파악해야 가지치기를 하던 뭘 하는데...
    def dfs(node, k, path):
        if k == 0:
            if node == end:
                result.append(path)
            return

        x, y = node
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if (not (0 <= n_x < n and 0 <= n_y < m)) or visited[k - 1][n_x][n_y] == 1:
                continue
            visited[k - 1][n_x][n_y] = 1
            dfs((n_x, n_y), k - 1, path + path_alpha[i])

    # 사전순을 따지면 아래(d), 왼쪽(l), 오른쪽(r), 위쪽(u)
    # 최대한 사전순으로 움직였으면 하는 것이다?
    # 판의 크기는 최대 50 * 50
    # 어쨋든 탐색이 이루어져야하고 방문했던 지점을 다시 방문해도 된다... 다만 총 k번 횟수만에 목적지에 도착해야한다.
    path_alpha = {0: "d", 1: "l", 2: "r", 3: "u"}
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    start = (x - 1, y - 1)
    end = (r - 1, c - 1)

    result = []
    visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
    visited[k][start[0]][start[1]] = 1
    dfs(start, k, "")
    result.sort()
    return result[0] if result else "impossible"