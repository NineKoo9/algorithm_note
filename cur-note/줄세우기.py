from collections import deque
def solution():
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]

    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    for a, b in info: # a가 b 앞에 서야한다.
        graph[a].append(b)
        in_degree[b] += 1

    result = []
    q = deque()
    # 진입 차수가 0인 녀석을 모두 넣음
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)

        for next_node in graph[now]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)
    print(*result)

solution()