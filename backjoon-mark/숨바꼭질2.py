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



solution()