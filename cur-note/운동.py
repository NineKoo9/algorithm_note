def solution():
    V, E = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(E)]
    INF = int(1e9)
    graph = [[INF] * V for _ in range(V)]
    for start, end, dist in roads:
        graph[start - 1][end - 1] = dist
    for k in range(V):
        for s in range(V):
            for e in range(V):
                if graph[s][e] > graph[s][k] + graph[k][e]:
                    graph[s][e] = graph[s][k] + graph[k][e]
    min_dist = INF
    for i in range(V):
        min_dist = min(min_dist, graph[i][i])
    print(min_dist if min_dist != INF else -1)


solution()