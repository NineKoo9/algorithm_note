def solution():
    import heapq
    
    V, E = map(int, input().split()) # 정점의 갯수 2만 이하, 간선의 갯수 30만 이하
    K = int(input()) # 시작 정점의 번호
    infos = [map(int, input().split()) for _ in range(E)]
    INF = int(1e9)
    distance = [INF] * (V + 1) # 
    graph = [[] for _ in range(V+1)] # [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]
    for start, end, cost in infos:
        graph[start].append((end, cost))
    
    def dijkstra(start):
        distance[start] = 0
        q = []
        heapq.heappush(q, (distance[start], start)) # 이렇게 하면 거리가 짧은 순으로 나오겠지?
        while q:
            cost, node = heapq.heappop(q)
            # 여기에 가지치기를 위한 조건을 넣는다..? 거리가 다르다면 그 원소를 버리는 처리를 해줘야 한다? 아하... 큐에는 업데이트된 여러 경우가 들어갈 수 있는데... 한 점까지의 거리가 2번 업데이트 되어서 들어갔을 수 있지
            if distance[node] < cost:
                continue
            
            for n_node, n_cost in graph[node]:
                if distance[n_node] > n_cost + cost:
                    distance[n_node] = n_cost + cost
                    heapq.heappush(q, (distance[n_node], n_node))
            # 하지만 여기서 이미 처리된 적 잇는 노드라면 무시라는 조건이 들어가는데.... 왜?
        
    
    dijkstra(K)
    for d in distance[1:]:
        print(d) if d is not INF else print("INF")


# solution()

def solution():
    import heapq
    
    def dijkstra(start):
        distance[start] = 0
        q = []
        heapq.heappush(q, (distance[start], start))
        while q:
            cost, node = heapq.heappop(q)
            if distance[node] < cost:
                continue
            
            for n_node, n_cost in graph[node]:
                if distance[n_node] > n_cost + cost:
                    distance[n_node] = n_cost + cost
                    heapq.heappush(q, (distance[n_node], n_node))        
    
    V, E = map(int, input().split()) 
    K = int(input()) 
    infos = [map(int, input().split()) for _ in range(E)]
    INF = int(1e9)
    distance = [INF] * (V + 1) # 
    graph = [[] for _ in range(V+1)]
    for start, end, cost in infos:
        graph[start].append((end, cost))
    
    
    dijkstra(K)
    for d in distance[1:]:
        print(d if d != INF else "INF")

solution()