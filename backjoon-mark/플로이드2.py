def solution():
    n = int(input())
    m = int(input())
    bus_infos = [list(map(int, input().split())) for _ in range(m)]
    INF = int(1e9)
    # 이번에는 그냥 모두 dic 으로 가볼까?
    bus_cost_board = {i:{j:INF for j in range(1, n + 1)} for i in range(1, n + 1)}
    bus_path_board = {i:{j:0 for j in range(1, n + 1)} for i in range(1, n + 1)}
    # 먼저 최소비용을 초기화한다.
    for s, e, c in bus_infos:
        if bus_cost_board[s][e] > c:
            bus_cost_board[s][e] = c
            bus_path_board[s][e] = e
            
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                if bus_cost_board[i][j] > bus_cost_board[i][k] + bus_cost_board[k][j]:
                    bus_cost_board[i][j] = bus_cost_board[i][k] + bus_cost_board[k][j]
                    bus_path_board[i][j] = bus_path_board[i][k] # 이 부분이 핵심이네...
    # INF 인 곳은 0 으로 바꾸자
    for i in range(1, n+1):
        for j in range(1, n+1):
            if bus_cost_board[i][j] == INF:
                bus_cost_board[i][j] = 0
    # 최소비용값을 출력하자
    for i in range(1, n+1):
        print(" ".join(map(str, [bus_cost_board[i][j] for j in range(1, n+1)])))
    # 경로를 복원하여 출력하자.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if bus_cost_board[i][j] == 0:
                print(0)
                continue
            path = [1, i]
            n_i = i
            # 이젠 i 에서 j 로 가는 경로를 구해야 한다.
            while bus_path_board[n_i][j] != j:
                n_i = bus_path_board[n_i][j]
                path.append(n_i)
            path.append(j)
            path[0] = len(path) - 1
            print(" ".join(map(str, path)))
            
            
solution()