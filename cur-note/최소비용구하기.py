def solution():
    N = int(input()) # 도시의 갯수 최대 1000개
    M = int(input()) # 버스의 갯수 100,000 개
    bus_infos = [list(map(int, input().split())) for _ in range(M)]
    start, end = map(int, input().split())
    # 그래프를 초기화해보자.
    bus_graph = {i:[] for i in range(1, N + 1)} # 다익스트라를 쓸려면 우선 그래프가 필요하다. 한점에서 다른 점들로 연결된 정보.
    for s, e, c in bus_infos:
        bus_graph[s].append((e, c))
    # 최소비용을 담을 자료구조도 필요하다.
    INF = int(1e9)
    costs = [INF] * (N + 1)
    def dijkstra(node):
        import heapq
        
        costs[node] = 0
        q = []
        heapq.heappush(q, (costs[node], node))
        while q:
            cost, node = heapq.heappop(q)
            # 처리가 된 녀석이라면 제외하지?
            if costs[node] < cost:
                continue
            
            for n_node, n_cost in bus_graph[node]:
                if costs[n_node] > n_cost + cost:
                    costs[n_node] = n_cost + cost
                    heapq.heappush(q, (costs[n_node], n_node))
    
    dijkstra(start)
    
    print(costs[end])


solution()