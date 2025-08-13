def solution():
    from collections import deque
    N, K = map(int, input().split())
    # N 에서 K로 가는 가장 빠른 시간?
    # 기본적으로 완전탐색이 아닌가?
    visited = [0] * 100001

    q = deque()
    visited[N] = 1
    q.append((N, 0))
    while q:
        cur_point, second = q.popleft()
        if cur_point == K:
            print(second)
            break
        if (0 <= cur_point * 2 < len(visited)) and visited[cur_point * 2] == 0:
            visited[cur_point * 2] = 1
            q.append((cur_point * 2, second))
        if (0 <= cur_point - 1 < len(visited)) and visited[cur_point - 1] == 0:
            visited[cur_point - 1] = 1
            q.append((cur_point - 1, second + 1))
        if (0 <= cur_point + 1 < len(visited)) and visited[cur_point + 1] == 0:
            visited[cur_point + 1] = 1
            q.append((cur_point + 1, second + 1))

def solution2():
    import heapq
    N, K = map(int, input().split())
    visited = [False] * 100001

    pq = []
    visited[N] = True
    heapq.heappush(pq, (0, N))
    while pq:
        second, cur_point = heapq.heappop(pq)
        if cur_point == K:
            print(second)
            break
        for i, next_point in enumerate([cur_point * 2, cur_point + 1, cur_point - 1]):
            if not (0 <= next_point < 100001):
                continue
            if visited[next_point]:
                continue
            visited[next_point] = True
            heapq.heappush(pq, (second if i == 0 else second + 1, next_point))

solution2()
