from collections import deque
import sys

sys.setrecursionlimit(100000)
def solution():
    def get_max_node(node, dist):
        max_node = node
        max_dist = dist

        for n_node, n_dist in graph[node]:
            if visited[n_node]:
                continue
            visited[node] = 1
            n, d = get_max_node(n_node, dist + n_dist)
            if d > max_dist:
                max_node = n
                max_dist = d

        return max_node, max_dist

    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        parent, child, cost = map(int, input().split())
        graph[parent].append((child, cost))
        graph[child].append((parent, cost))

    # 임의의 한점에서 가장 먼 점은 어떻게 구할까?
    start = 1
    visited = [0] * (N + 1)
    node, dist = get_max_node(start, 0)

    # 그렇다면 이제 node에서 가장 먼 거리를 찾으면 되겠다!
    visited = [0] * (N + 1) # 하... 이걸 다시 초기화를 안했네...
    answer_node, answer_dist = get_max_node(node, 0)
    print(answer_dist if start != answer_node else dist)


solution()