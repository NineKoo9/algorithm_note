from collections import defaultdict, deque

def solution():
    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())
        lines = [tuple(map(int, input().split())) for _ in range(E)]
        graph = defaultdict(list)
        for u, v in lines:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        visited = [0] * V
        result = ""
        # 그래프가 분리되어 있다면 어떻게 하지? 모든 점에 다 수행하면 되지
        for node in range(V):
            if visited[node] != 0:
                continue
            q = deque()
            visited[node] = 1
            q.append((node, 1))
            flag = True
            while q and flag:
                cur_node, team = q.popleft()

                for n_node in graph[cur_node]:
                    if visited[n_node] == 0:
                        visited[n_node] = team * -1
                        q.append((n_node, team * -1))
                    elif visited[n_node] == team:
                        result = "NO"
                        flag = False
                        break
        if result != "NO":
            print("YES")
        else:
            print("NO")

    pass


solution()