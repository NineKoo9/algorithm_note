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

    V = int(input())

    # 그래프 초기화
    graph = [[] for _ in range(V + 1)]
    for _ in range(V):
        q = deque(map(int, input().split()))
        v = q.popleft()
        while len(q) > 1:
            node = q.popleft()
            dist = q.popleft()
            graph[v].append((node, dist))
            graph[node].append((v, dist))

    # 임의의 한점에서 가장 먼 점은 어떻게 구할까?
    start = 1
    visited = [0] * (V + 1)
    node, dist = get_max_node(start, 0)

    # 그렇다면 이제 node에서 가장 먼 거리를 찾으면 되겠다!
    visited = [0] * (V + 1) # 하... 이걸 다시 초기화를 안했네...
    answer_node, answer_dist = get_max_node(node, 0)
    print(answer_dist if start != answer_node else dist)


solution()