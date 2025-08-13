def solution(n, s, a, b, fares):  # n지점의 갯수, s 출발지점, a의 집, b의 집, fares 요금
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    # 자기자신으로 가는 경로는 0으로 할 필요가 있겠다.
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    graph[i][j] = 0
                    continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return min(graph[s][i] + graph[i][a] + graph[i][b] for i in range(1, n + 1))