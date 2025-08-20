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
    
    
def solution2():
    import heapq
    
    def dijkstra(node):
        q = []
        heapq.heappush(q, (0, node))
        x_to_node_costs[node] = 0
        
        while q:
            cur_cost, cur_node = heapq.heappop(q)
            if x_to_node_costs[cur_node] < cur_cost:
                continue
            
            for nxt_node, nxt_cost in graph[cur_node]:
                if nxt_cost + cur_cost < x_to_node_costs[nxt_node]:
                    x_to_node_costs[nxt_node] = nxt_cost + cur_cost
                    q.append((nxt_cost + cur_cost, nxt_node))
    
    def dijkstra2(node):
        q = []
        heapq.heappush(q, (0, node))
        node_to_x_costs[node] = 0
        
        while q:
            cur_cost, cur_node = heapq.heappop(q)
            if node_to_x_costs[cur_node] < cur_cost:
                continue
            
            for prev_node, prev_cost in in_graph[cur_node]:
                if prev_cost + cur_cost < node_to_x_costs[prev_node]:
                    node_to_x_costs[prev_node] = prev_cost + cur_cost
                    q.append((prev_cost + cur_cost, prev_node))
        
        
    N, M, X = map(int, input().split())
    
    graph = [[] for _ in range(N + 1)]
    in_graph = [[] for _ in range(N + 1)] # 이것을 만들어서 확인할 수 있겠다는 생각을 잠깐 못했다.
    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))
        in_graph[e].append((s, c))
    
    INF = int(1e9)
    x_to_node_costs = [INF] * (N + 1)
    node_to_x_costs = [INF] * (N + 1) # 이것도 어쨋든 한점과 여러점의 차이잖아?
    dijkstra(X) # 먼저 X에서 모든 점까지의 비용을 구한다.
    dijkstra2(X)
    total = [c1 + c2 for c1, c2 in zip(x_to_node_costs[1:], node_to_x_costs[1:])]
    print(max(total))
    
        
solution2()

