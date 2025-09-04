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
            
            
def solution2():
    n = int(input())
    m = int(input())
    bus_infos = [list(map(int, input().split())) for _ in range(m)]
    
    # 모든 점에서 모든 점까지의 최소 비용을 구해야하니까 플로이드 워샬 알고리즘이 적절하다.
    # 최소비용 경로에 포함되어 있는 도시의 수, 그리고 그 경로를 나란히 출력한다
    INF = int(1e9)
    cost_board = [[INF] * (n + 1) for _ in range(n + 1)]
    path_board = [[INF] * (n + 1) for _ in range(n + 1)] # 이것을 처음에 무엇으로 초기화하지?
    
    # 먼저 단일로 갈 수 있는 비용을 넣어준다.
    for start, end, cost in bus_infos:
        if cost_board[start][end] > cost:
            cost_board[start][end] = cost
            path_board[start][end] = end
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j or i == k or j == k:
                    continue
                if cost_board[i][j] > cost_board[i][k] + cost_board[k][j]:
                    cost_board[i][j] = cost_board[i][k] + cost_board[k][j]
                    path_board[i][j] = path_board[i][k]
    
                
    # 이제 첫번째 결과를 출력한다.
    for i in range(1, n + 1):
        out = ""
        for j in range(1, n + 1):
            out += (str(cost_board[i][j]) if cost_board[i][j] != INF else "0") + " "
        print(out[:-1])
    
    # 이제 경로를 출력해보자.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 이제 i에서 j까지 가는 경로를 모두 출력해야한다.
            # 경로를 복원해야하는데...
            if cost_board[i][j] == INF:
                print(0)
                continue
            # 이제 길이 있다면 출력한다.
            out = [1, i]
            n_i = i
            while n_i != j:
                n_i = path_board[n_i][j]
                out.append(n_i)
            out[0] = len(out) - 1
            print(" ".join(map(str, out)))
                
solution2()