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


        
        