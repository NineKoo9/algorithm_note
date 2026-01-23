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

def solution2():
    import heapq
    
    N, M = map(int, input().split())
    priority_orders = [list(map(int, input().split())) for _ in range(M)]
    
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    for priority_order in priority_orders:
        a, b = priority_order
        graph[a].append(b)
        in_degree[b] += 1
        
    # 이제 위상정렬그래프는 완성되었는데, 그 다음은 어떻게 할까?
    # 어떻게 위상정렬 트리 안에 다른 관계없는 노드들을 탐색해나갈까?
    # 작은 것 부터 탐색해나가면서 만약 in_degree값이 0이 아니라면? 그러면 파고든다? 아니... 잠만
    # in_degree가 0인 녀석은... 일단 리프노드거나, 우선순위가 없는 것이 아닐까?
    # 그렇다면 in_degree인 녀석들은 문제 번호가 낮은 순서로 해도 되지 않을까?
    # 근데... 되도록이면 작은 순서로 해야하는데 아 여거시 우선순위 큐가 적용될 것 같다.
    q = []
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            heapq.heappush(q, i)
    
    answer = []
    while q:
        node = heapq.heappop(q)
        
        # 여기서 나온 node는 degree가 0이니까 먼저 풀어야할 문제가 없다고 할 수 있다.
        answer.append(node)
        
        for n_node in graph[node]:
            in_degree[n_node] -= 1
            if in_degree[n_node] == 0:
                heapq.heappush(q, n_node)
    print(*answer)
    
solution2()