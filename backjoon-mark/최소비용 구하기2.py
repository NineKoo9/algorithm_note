def solution():
    n = int(input()) # 도시의 개수 1000 이하
    m = int(input()) # m개의 버스 10만 이하
    bus_infos = [map(int, input().split()) for _ in range(m)]
    start, end = map(int, input().split())
    graph = [[] for _ in range(n + 1)] # 도시의 수가 n개 라면... 번호를 1번부터 매긴다.
    for s, e, c in bus_infos:
        graph[s].append((e, c))
    
    INF = int(1e9)
    distance = [INF] * (n + 1)
    pre_table = [i for i in range(n+1)] # pre_table의 초기값은 뭘로하지?
    
    def dijkstra(s):
        import heapq
        
        distance[s] = 0
        q = []
        heapq.heappush(q, (distance[s], s))
        while q:
            cost, node = heapq.heappop(q)
            if distance[node] < cost:
                continue
            for n_node, n_cost in graph[node]:
                if distance[n_node] > n_cost + cost:
                    distance[n_node] = n_cost + cost
                    pre_table[n_node] = node
                    heapq.heappush(q, (distance[n_node], n_node))

    dijkstra(start)
    path = [end]
    now = end
    while now != start:
        now = pre_table[now]
        path.append(now)
    
    
    print(distance[end])
    print(len(path))
    print(" ".join(map(str, path[::-1])))

import heapq
def solution2():

    n = int(input())
    m = int(input())
    bus_infos = [list(map(int, input().split())) for _ in range(m)]
    src, dest = map(int, input().split())

    graph = {}
    for start, end, cost in bus_infos:
        if start not in graph:
            graph[start] = {end: cost}
        else:
            graph[start][end] = cost
    print(graph)
    INF = int(1e9)
    prev_path = {i: i for i in range(1, n + 1)}
    distance = {i: INF for i in range(1, n + 1)}
    distance[src] = 0
    q = [(0, src)]
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n_node in graph[node].keys():
            if distance[n_node] > dist + graph[node][n_node]:
                distance[n_node] = dist + graph[node][n_node]
                prev_path[n_node] = node
                heapq.heappush(q, (distance[n_node], n_node))
    print(distance[dest])
    # 이제부터 경로를 복원해야한다.
    path = [dest]
    point = dest
    while point != src:
        prev_node = prev_path[point]
        path.append(prev_node)
        point = prev_node
    print(prev_path)

def solution3():
    import heapq

    n = int(input())
    m = int(input())
    bus_lines = [list(map(int, input().split())) for _ in range(m)]
    start, dest = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for s, e, c in bus_lines:
        graph[s].append((e, c))
    # 이제부터 start에서 dest까지 최소비용으로 가기위한 것은?

    INF = int(1e9)
    dp = [INF] * (n + 1)
    h = []
    prev_node = [i for i in range(n + 1)]
    heapq.heappush(h, (0, start))
    dp[start] = 0
    while h:
        dist, node = heapq.heappop(h)
        if dp[node] < dist:
            continue
        for n_node, cost in graph[node]:
            if dp[n_node] > dist + cost:
                prev_node[n_node] = node
                dp[n_node] = dist + cost
                heapq.heappush(h, (dp[n_node], n_node))

    print(dp[dest])
    # 자 이제 경로 복원을 하자.
    paths = [dest]
    now = dest
    while now != prev_node[now]:
        prev = prev_node[now]
        paths.append(prev)
        now = prev
    print(len(paths))
    print(*paths[::-1])


solution3()