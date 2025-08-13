from collections import defaultdict, deque
def solution():
    def dfs(node):
        if visited_for_dfs[node]:
            return
        visited_for_dfs[node] = 1
        dfs_result.append(node)
        for next_node in sorted(graph[node]):
            dfs(next_node)

    def bfs(start):
        visited_for_bfs[start] = 1
        bfs_result.append(start)
        q = deque()
        q.append(start)
        while q:
            current_node = q.popleft()
            for next_node in sorted(graph[current_node]):
                if visited_for_bfs[next_node]:
                    continue
                visited_for_bfs[next_node] = 1
                bfs_result.append(next_node)
                q.append(next_node)

    N, M, V = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(M)]
    graph = defaultdict(list)
    for node1, node2 in A:
        graph[node1].append(node2)
        graph[node2].append(node1)
    visited_for_bfs = {i: 0 for i in range(1, N + 1)}
    visited_for_dfs = {i: 0 for i in range(1, N + 1)}
    bfs_result = []
    dfs_result = []
    dfs(V)
    bfs(V)
    print(*dfs_result)
    print(*bfs_result)

solution()