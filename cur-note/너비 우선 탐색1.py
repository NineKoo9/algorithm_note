from collections import defaultdict, deque

def solution():
    def bfs(node):
        q = deque()
        order = 1
        visited[node] = 1
        visit_order[node] = order
        q.append(node)
        while q:
            current_node = q.popleft()
            for next_node in graph[current_node]:
                if visited[next_node]:
                    continue
                order += 1
                visited[next_node] = 1
                visit_order[next_node] = order
                q.append(next_node)


    N, M, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    graph = defaultdict(list)
    for node1, node2, in sorted(A):
        graph[node1].append(node2)
        graph[node2].append(node1)
    visited = {i: 0 for i in range(1, N + 1)}
    visit_order = {i: 0 for i in range(1, N + 1)}
    bfs(R)
    for k, v in visit_order.items():
        print(v)


solution()