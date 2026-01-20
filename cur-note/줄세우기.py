from collections import deque
def solution():
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]

    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    for a, b in info: # a가 b 앞에 서야한다.
        graph[a].append(b)
        in_degree[b] += 1

    result = []
    q = deque()
    # 진입 차수가 0인 녀석을 모두 넣음
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)

        for next_node in graph[now]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)
    print(*result)

def solution2():
    from collections import deque
    
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
        
    # 일단 indegree가 0인 녀석들은 끝 노드니까 q에 추가한다.
    q = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)
        
    ordered_result = []    
    while q:
        node = q.popleft()
        ordered_result.append(node)
        
        for n_node in graph[node]:
            
            # 차수를 감소시키면서 그래프를 제거해본다.
            in_degree[n_node] -= 1
            
            # 만약 루트노드가 된다면 q에 넣어서 탐색한다.
            if in_degree[n_node] == 0:
                q.append(n_node)
    print(*ordered_result)


solution2()