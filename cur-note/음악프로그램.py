from collections import deque

def solution():
    # 이 문제는 위상정렬을 활용하면 풀릴 것 같다.
    N, M = map(int, input().split())  # 가수의 수
    single_orders = [list(map(int, input().split())) for _ in range(M)]

    in_degree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    for single_order in single_orders:
        prev = single_order[1]
        for single in single_order[2:]:
            graph[prev].append(single)
            in_degree[single] += 1
            prev = single
    # 진입차수가 0인 녀석들을 초기화한다.
    q = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    result = []
    while q:
        node = q.popleft()

        result.append(node)

        for n_node in graph[node]:
            in_degree[n_node] -= 1
            if in_degree[n_node] == 0:
                q.append(n_node)
    for i in range(1, N + 1):
        if in_degree[i] != 0:
            print(0)
            exit()

    print(*result, sep="\n")

solution()