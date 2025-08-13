from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 5)


def solution():
    def dfs(node, count):
        visited[node] = 1
        node_order[node] = count
        for next_node in graph[node]:
            if visited[next_node]:
                continue
            count = dfs(next_node, count + 1)
        return count

    N, M, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    graph = defaultdict(list)
    for node1, node2 in sorted(A, reverse=True):
        graph[node1].append(node2)
        graph[node2].append(node1)
    visited = {i: 0 for i in range(1, N + 1)}
    node_order = {i: 0 for i in range(1, N + 1)}
    dfs(R, 1)
    for k, v in node_order.items():
        print(v)


solution()
