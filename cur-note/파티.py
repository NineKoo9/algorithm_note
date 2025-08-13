def solution():
    import heapq
    
    N, M, X = map(int, input().split()) # N명의 학생 N개의 마을에 살음. M개의 단방향 도로, X 마을에 모임
    infos = [map(int, input().split()) for _ in range(M)]
    graph = [[] for _ in range(N + 1)]
    in_graph = [[] for _ in range(N + 1)] # 어떤 도착점까지 들어오는 노드들의 비용을 표현한다.
    for s, e, t in infos:
        graph[s].append((e, t))
        in_graph[e].append((s, t))
        
    INF = int(1e9)
    out_distance = [INF] * (N + 1)
    in_distance = [INF] * (N + 1)
    
    def dijkstra(start):
        q = []
        out_distance[start] = 0
        heapq.heappush(q, (out_distance[start], start))
        while q:
            cost, node = heapq.heappop(q)
            if out_distance[node] < cost:
                continue
            for n_node, n_cost in graph[node]:
                if out_distance[n_node] > n_cost + cost:
                    out_distance[n_node] = n_cost + cost
                    heapq.heappush(q, (out_distance[n_node], n_node))
                    
    def in_dijkstra(end):
        q = []
        in_distance[end] = 0
        heapq.heappush(q, (in_distance[end], end))
        while q:
            cost, node = heapq.heappop(q)
            if in_distance[node] < cost:
                continue
            for in_node, in_cost in in_graph[node]:
                if in_distance[in_node] > in_cost + cost:
                    in_distance[in_node] = in_cost + cost
                    heapq.heappush(q, (in_distance[in_node], in_node))
    
    dijkstra(X)
    in_dijkstra(X)
    result = [a + b for a, b in zip(out_distance[1:], in_distance[1:])]
    return max(result)
    
print(solution())