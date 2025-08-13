import sys

sys.setrecursionlimit(10**5)
def solution():
    from collections import defaultdict

    def dfs(node, count):
        visited[node] = 1
        node_order[node] = count
        for next_node in graph[node]:
            if visited[next_node]:
                continue
            count = dfs(next_node, count + 1)
        return count

    N, M, R = map(int, input().split())
    Array = [list(map(int, input().split())) for _ in range(M)]
    graph = defaultdict(list)
    visited = [0] * (N + 1)
    node_order = [0] * (N + 1)
    for node1, node2 in sorted(Array):
        graph[node1].append(node2)
        graph[node2].append(node1)
    dfs(R, 1)
    print(*node_order[1:], sep="\n")

solution()