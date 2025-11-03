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


from collections import deque

def solution2(n, m, r1, c1, r2, c2, k):
    # 먼저 못가는 경우
    diff = k - abs(r2 - r1) - abs(c2 - c1)
    if diff % 2 != 0 or diff < 0: # 아에 못가는 경우도 고려해야하군...
        return "impossible"
    
    # 이제 갈 수 있는 경우
    orders = ["d", "l", "r", "u"]
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    
    q = deque()
    q.append((r1, c1, k, ""))
    visited = [[[0] * (m + 1) for _ in range(n + 1)] for i in range(k + 1)]
    visited[k][r1][c1] = 1
    while q:
        r, c, count, path = q.popleft()
        
        if r == r2 and c == c2 and count == 0:
            return path
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (not (0 < nr <= n and 0 < nc <= m)) or count <= 0 or visited[count - 1][nr][nc]:
                continue
            visited[count - 1][nr][nc] = 1
            q.append((nr, nc, count - 1, path + orders[i]))
    
# 이건 제미니 풀이다.
def solution3(n, m, r1, c1, r2, c2, k):
    # 1. 시작부터 불가능한 경우 판별
    manhattan_dist = abs(r1 - r2) + abs(c1 - c2)
    if (k - manhattan_dist) % 2 != 0 or k < manhattan_dist:
        return "impossible"

    # 2. 그리디 탐색 시작
    path = []
    cr, cc = r1, c1  # 현재 위치 (current row, current col)
    
    # 방향 우선순위: d, l, r, u
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    orders = ["d", "l", "r", "u"]

    for moves_left in range(k, 0, -1):
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            # 맵을 벗어나는지 확인
            if not (1 <= nr <= n and 1 <= nc <= m):
                continue

            # '가능한 이동'인지 확인
            dist_to_target = abs(nr - r2) + abs(nc - c2)
            if dist_to_target <= moves_left - 1 and (moves_left - 1 - dist_to_target) % 2 == 0:
                path.append(orders[i])
                cr, cc = nr, nc
                break # 최적의 방향을 찾았으므로 다음 이동으로 넘어감
    
    return "".join(path)