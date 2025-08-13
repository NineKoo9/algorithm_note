def solution():
    N, E = map(int, input().split())
    infos = [map(int, input().split()) for _ in range(E)]
    u, v = map(int, input().split())
    INF = int(1e9)
    graph = [[-1] * (N + 1) for _ in range(N + 1)]
    for a, b, c in infos:
        graph[a][b] = c
        graph[b][a] = c
    start_min_distance = [INF] * (N + 1)
    vertex1_min_distance = [INF] * (N + 1)
    vertex2_min_distance = [INF] * (N + 1)
    def dijkstra(start, min_distance):
        import heapq
        
        min_distance[start] = 0
        q = []
        heapq.heappush(q, (min_distance[start], start))
        while q:
            dist, node = heapq.heappop(q)
            if min_distance[node] < dist:
                continue
            for n_node, n_dist in enumerate(graph[node][1:], start=1):
                if n_dist == -1:
                    continue
                if min_distance[n_node] > dist + n_dist:
                    min_distance[n_node] = dist + n_dist
                    heapq.heappush(q, (min_distance[n_node], n_node))
    
    dijkstra(1, start_min_distance)
    dijkstra(u, vertex1_min_distance)
    dijkstra(v, vertex2_min_distance)
    result = min(start_min_distance[u] + vertex1_min_distance[v] + vertex2_min_distance[N],
              start_min_distance[v] + vertex1_min_distance[v] + vertex1_min_distance[N])
    print(result if result < INF else -1)

solution()