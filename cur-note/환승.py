from collections import defaultdict, deque
def solution():
    N, K, M = map(int, input().split())  # 역의 수, 하이퍼튜브가 서로 연결하는 수, 하이퍼튜브의 갯수
    hyper_tube_infos = [input().split() for _ in range(M)]

    # 이 그래프를 어떻게 구현할까? 하이퍼튜브 노드는 문자열로하고...
    # 나머지 노드에 대해서는 어떻게 할까? 한번더 포문을 돌면 되는데... 이런 초기화방식 낯설어서 정말 어렵다.
    # 근데... 이렇게 키 값이 타입이 다르면... 자바에서는 문제가 되겠다.
    graph = defaultdict(list)
    for h in range(M):
        hyper_node = "h" + str(h)
        graph[hyper_node] = hyper_tube_infos[h]
        for i in range(K):
            graph[hyper_tube_infos[h][i]].append(hyper_node)

    # 이제부터 bfs로 1번부터 탐색하면 되겠다.
    start = "1"
    end = str(N)

    visited = {k: 0 for k in graph.keys()}
    q = deque()
    q.append((start, 1))
    visited[start] = 1
    while q:
        node, dist = q.popleft()
        if node == end:
            print(dist)
            exit()

        for n_node in graph[node]:
            if visited[n_node]:
                continue

            visited[n_node] = 1
            if n_node.isdigit():
                q.append((n_node, dist + 1))
            else: # 숫자가 아니면 하이퍼튜브지
                q.append((n_node, dist))
    print(-1)

solution()