from collections import deque

def solution():
    N, K = map(int, input().split())

    q = deque()
    q.append((N, 0))

    visited = [0] * 100001
    visited[N] = 1
    dist = [0] * 100001
    # 이게 몇개? 를 구해야하니까... 뭔가 이상하다?
    # 정답부분을 여러번 도착할 수 있잖아?
    min_time = int(1e9)
    cnt = 0
    while q:
        point, elapsed_time = q.popleft()

        if point == K:
            # 최소시간으로 도착해야하는데?
            min_time = elapsed_time
            cnt += 1
            continue

        for n_point in [point + 1, point - 1, point * 2]:
            # 범위를 벗어나면 아웃
            if not 0 <= n_point <= 100000:
                continue
            # 방문을 하지 않았다면 방문을 하면 된다.
            if visited[n_point] == 0:
                visited[n_point] = 1
                dist[n_point] = elapsed_time + 1
                q.append((n_point, elapsed_time + 1))
            # 하지만 예외적으로 다음 포인트가 현재 포인트와 거리가 일치한다면 방문을 허용한다.
            elif dist[n_point] == elapsed_time + 1:
                q.append((n_point, elapsed_time + 1))


    print(min_time)
    print(cnt)

def solution2():
    N, K = map(int, input().split())
    
    # 어쨋든 가장 빠른 시간으로 찾는 방법이 몇개인지 파악하는 것인데... 동일한 시간이 걸린다면, 그 가짓수가 몇개인지 구해야한다.
    # 생각해보니 여러개를 구하는 것이니까...
    # 최소거리를 구하는 것이라면... bfs로 탐색해나고도 된다.
    q = deque()
    visited = [False] * 100001
    fastest_sec = int(1e9)
    answer_count = 0
    q.append((N, 0))
    while q:
        point, elapsed_sec = q.popleft()
        visited[N] = True
        if point == K:
            # 정답을 찾음! 근데 현재의 큐에 동일한 sec을 가졌으면서 node에 도착할 수 있는 원소들이 있을 수 있다. 그것이 몇개인지 찾아야한다.
            fastest_sec = elapsed_sec
            answer_count += 1
            while q:
                point_a, elapsed_sec_a = q.popleft()
                if point_a == K and elapsed_sec_a <= fastest_sec:
                    answer_count += 1
            break
        
        for n_point in [point - 1, point + 1, point * 2]:
            if not 0 <= n_point <= 100000:
                continue
            if visited[n_point]:
                continue
            q.append((n_point, elapsed_sec + 1))
    
    print(fastest_sec)
    print(answer_count)

import sys
from collections import deque


# 이건 제미니가 작성해준 코드
def solution_fixed():
    # 빠른 입력을 위해 sys.stdin.readline 사용 권장
    input = sys.stdin.readline
    N, K = map(int, input().split())
    
    # 예외 처리: 시작점과 도착점이 같은 경우
    if N == K:
        print(0)
        print(1)
        return

    # visited 배열: 방문 여부뿐만 아니라 '해당 지점까지의 최단 시간'을 저장
    # 초기값은 -1 또는 무한대로 설정
    max_pos = 100000
    visited = [-1] * (max_pos + 1)
    
    queue = deque()
    queue.append((N, 0)) # (현재 위치, 경과 시간)
    visited[N] = 0
    
    answer_count = 0
    fastest_time = float('inf')
    
    while queue:
        current_pos, current_time = queue.popleft()
        
        # [가지치기] 이미 찾은 최단 시간보다 더 오래 걸리는 경우는 탐색할 필요 없음
        if current_time > fastest_time:
            break
            
        # 목표 지점 도착
        if current_pos == K:
            # 처음 도착했다면 최단 시간 갱신
            if fastest_time == float('inf'):
                fastest_time = current_time
                answer_count = 1
            # 이미 찾은 최단 시간과 같다면 카운트 증가
            elif current_time == fastest_time:
                answer_count += 1
            continue  # 도착했으면 더 이상 이 경로로 이동하지 않음
        
        # 이동 가능한 3가지 경우 탐색
        for next_pos in (current_pos - 1, current_pos + 1, current_pos * 2):
            if 0 <= next_pos <= max_pos:
                # [핵심 로직]
                # 1. 방문한 적이 없거나 (visited == -1)
                # 2. 방문한 적이 있어도, 지금 가는 시간이 기존 최단 시간과 같다면 (visited == current_time + 1)
                # 큐에 추가하여 경로를 인정해줌
                if visited[next_pos] == -1 or visited[next_pos] == current_time + 1:
                    visited[next_pos] = current_time + 1
                    queue.append((next_pos, current_time + 1))

    print(fastest_time)
    print(answer_count)

# 실행
solution_fixed()