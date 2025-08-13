import heapq

def solution():
    N, M = map(int, input().split())
    prerequisite = [list(map(int, input().split())) for _ in range(M)]

    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    for a, b in prerequisite:
        graph[a].append(b)
        in_degree[b] += 1

    # 이제 진입차수가 0인 녀석들을 모두 우선순위큐에 넣는다.
    h = []
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            heapq.heappush(h, i)

    result = []
    while h:
        now = heapq.heappop(h)
        result.append(now)

        for n_node in graph[now]:
            in_degree[n_node] -= 1
            if in_degree[n_node] == 0:
                heapq.heappush(h, n_node)
    print(*result)

    pass


solution()