from collections import defaultdict, deque
def solution():
    N, K, M = map(int, input().split())  # 역의 수, 하이퍼튜브가 서로 연결하는 수, 하이퍼튜브의 갯수
    hyper_tube_infos = [input().split() for _ in range(M)]

    # 이 그래프를 어떻게 구현할까? 하이퍼튜브 노드는 문자열로하고...
    # 나머지 노드에 대해서는 어떻게 할까? 한번더 포문을 돌면 되는데... 이런 초기화방식 낯설어서 정말 어렵다.
    # 근데... 이렇게 키 값이 타입이 다르면... 자바에서는 문제가 되겠다.
    graph = defaultdict(list)
    for h in range(M):
        hyper_node = "h" + str(h)
        graph[hyper_node] = hyper_tube_infos[h]
        for i in range(K):
            graph[hyper_tube_infos[h][i]].append(hyper_node)

    # 이제부터 bfs로 1번부터 탐색하면 되겠다.
    start = "1"
    end = str(N)

    visited = {k: 0 for k in graph.keys()}
    q = deque()
    q.append((start, 1))
    visited[start] = 1
    while q:
        node, dist = q.popleft()
        if node == end:
            print(dist)
            exit()

        for n_node in graph[node]:
            if visited[n_node]:
                continue

            visited[n_node] = 1
            if n_node.isdigit():
                q.append((n_node, dist + 1))
            else: # 숫자가 아니면 하이퍼튜브지
                q.append((n_node, dist))
    print(-1)

# 하이퍼튜브로 연결된 구간만 지날 수 있다가 되겠네
    # 하이퍼튜브 안에서는 각 역들이 연결되어 있으니 거리는 모두 1이다.
    # 만약 1000개를 연결하고 하이퍼튜브가 1000개 있다면? 총 간선이
    # 1000C2 * 1000개가 될 것이다.
    # 만약 하이퍼 튜브 하나를 각각의 노드로 생각한다면? 그래도 여전히 거치는 역의 갯수는
    # 1개로 같지 않나?
    # 어쨋든 서로 같은 하이퍼튜브냐 아니면 서로 다른 튜브냐를 구분해야하고...
    # 이 튜브에서 다른 튜브로 갈 수 있는지 아닌지를 확인해야한다.
import sys
from collections import deque

# 입력 속도를 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solution_fixed():
    N, K, M = map(int, input().split())
    
    # 그래프 초기화 (역: 1~N, 튜브: N+1 ~ N+M)
    graph = [[] for _ in range(N + M + 1)]
    
    for i in range(M):
        # 하이퍼튜브에 연결된 역들을 입력받음
        stations = list(map(int, input().split()))
        
        # 튜브 노드 번호 부여 (N + 1 부터 시작)
        tube_node = N + 1 + i
        
        for station in stations:
            # 역 <-> 튜브 양방향 연결
            graph[station].append(tube_node)
            graph[tube_node].append(station)

    # BFS 탐색
    # visited 배열에 '방문 여부' 혹은 '거리' 저장
    # 0이면 미방문, 0보다 크면 방문한 역의 개수
    visited = [0] * (N + M + 1)
    
    q = deque()
    q.append(1)      # 1번 역에서 시작
    visited[1] = 1   # 시작할 때 역 개수는 1개
    
    while q:
        curr = q.popleft()
        
        # 목적지 도착 확인
        if curr == N:
            print(visited[curr])
            return

        for nxt in graph[curr]:
            if visited[nxt] == 0: # 아직 방문 안 했다면
                if nxt > N: 
                    # 다음 노드가 튜브인 경우 (역 -> 튜브)
                    # 튜브 환승은 역 개수에 포함되지 않으므로 비용 유지
                    visited[nxt] = visited[curr] 
                    q.append(nxt)
                else:
                    # 다음 노드가 역인 경우 (튜브 -> 역)
                    # 새로운 역을 밟았으므로 역 개수 + 1
                    visited[nxt] = visited[curr] + 1
                    q.append(nxt)
                    
    # 도달할 수 없는 경우
    print(-1)

solution_fixed()