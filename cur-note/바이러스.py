from collections import defaultdict
def solution():
    def dfs(node):
        if visited[node]:
            return
        visited[node] = 1
        for next_node in network[node]:
            dfs(next_node)


    N = int(input())
    M = int(input())
    A = [list(map(int, input().split())) for _ in range(M)]
    network = defaultdict(list)
    for node1, node2 in A:
        network[node1].append(node2)
        network[node2].append(node1)

    visited = [0] * (N + 1)
    dfs(1)
    print(sum(visited) - 1)

solution()