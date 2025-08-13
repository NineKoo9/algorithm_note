def solution():
    n = int(input())
    m = int(input())
    bus_infos = [list(map(int, input().split())) for _ in range(m)]
    INF = int(1e9)
    bus_cost_graph = [[INF] * n for _ in range(n)]
    for s, e, c in bus_infos:
        if bus_cost_graph[s-1][e-1] > c:
            bus_cost_graph[s-1][e-1] = c
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or k == j: # 이 부분 체크하자... 자기자신에서 자기자신...
                    continue
                if bus_cost_graph[i][j] > bus_cost_graph[i][k] + bus_cost_graph[k][j]:
                    bus_cost_graph[i][j] = bus_cost_graph[i][k] + bus_cost_graph[k][j]
                    
    for row in bus_cost_graph:
        print(" ".join(map(str, [i if i < INF else 0 for i in row])))

solution()