class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 가장 최소가 되는 트리의 루트를 찾을려면... 가장 바깥쪽 부터 안쪽으로 그래프를 탐색해야한다.
        # 그렇게 가장 가운데에 있는 녀석들을 찾아야한다.
        # 그럴려면 리프노드를 구해야하는데... 어케하지?
        leaf_nodes = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaf_nodes.append(i)
        while n > 2:
            n -= len(leaf_nodes)
            new_leaf_nodes = []
            for leaf_node in leaf_nodes:
                neighbor = graph[leaf_node].pop()
                graph[neighbor].remove(leaf_node)

                if len(graph[neighbor]) == 1:
                    new_leaf_nodes.append(neighbor)
            leaf_nodes = new_leaf_nodes
        return leaf_nodes


class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaf_nodes = []
        # 리프노드들을 구해보자.
        for node in range(n):
            if len(graph[node]) == 1:
                leaf_nodes.append(node)

        while n > 2:  # 남은 노드의 수가 1개 또는 2개가 되면 그때가 끝이다.
            n -= len(leaf_nodes)

            new_leaf_nodes = []
            for leaf_node in leaf_nodes:
                n_node = graph[leaf_node].pop()
                graph[n_node].remove(leaf_node)
                if len(graph[n_node]) == 1:
                    new_leaf_nodes.append(n_node)
            leaf_nodes = new_leaf_nodes
        return leaf_nodes


from collections import deque

class Solution3:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def find_furthest_node_with_path(node: int):
            furthest_node, furthest_dist = node, 0
            
            q = deque()
            visited = [False] * n
            parent = [i for i in range(n)]

            visited[node] = True
            q.append((node, 0))
            while q:
                cur_node, dist = q.popleft()
                for n_node in graph[cur_node]:
                    if visited[n_node]:
                        continue
                    visited[n_node] = True
                    if dist + 1 >= furthest_dist:
                        furthest_dist = dist + 1
                        furthest_node = n_node
                        parent[n_node] = cur_node
                    q.append((n_node, dist + 1))
            
            cur = furthest_node
            path = [furthest_node]
            while parent[cur] != cur:
                nxt = parent[cur]
                path.append(nxt)
                cur = nxt

            return furthest_node, path[::-1]

        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        node_a, _ = find_furthest_node_with_path(0)
        node_b, path = find_furthest_node_with_path(node_a)
        l = len(path)
        if l % 2 == 0:
            mid = l // 2
            return [path[mid - 1], path[mid]]
        else:
            mid = l // 2
            return [path[mid]]


        
# 이건 차수를 다루는 풀이이다.
class Solution4:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # 예외 처리: 노드가 1개일 때
        if n == 1:
            return [0]
        
        # 1. 그래프(인접 리스트)와 차수(Degree) 리스트 초기화
        graph = [[] for _ in range(n)]
        degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        # 2. 첫 번째 리프 노드들(차수가 1인 노드)을 큐에 담기
        leaves = deque([i for i in range(n) if degree[i] == 1])
        
        # 3. 리프 노드 깎기 (남은 노드가 2개 이하가 될 때까지 반복)
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count # 현재 단계에서 제거할 리프 노드 수만큼 감소
            
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                
                # 리프 노드와 연결된 이웃 노드 처리
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1 # 간선을 끊는 대신 차수만 감소
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
                        
        return list(leaves)