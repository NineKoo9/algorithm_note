from collections import deque
def solution():
    N, K = map(int, input().split())
    visited = 0b0
    q = deque()
    visited = visited | 1 << N
    q.append((N, 0))
    while q:
        node, time = q.popleft()
        if node == K:
            print(time)
            break

        if node - 1 >= 0 and ((visited & (1 << (node - 1))) == 0):
            visited = visited | (1 << (node - 1))
            q.append((node - 1, time + 1))
        if node + 1 < 100001 and ((visited & (1 << (node + 1))) == 0):
            visited = visited | (1 << (node + 1))
            q.append((node + 1, time + 1))
        if 0 <= 2 * node < 100001 and ((visited & (1 << (2 * node))) == 0):
            visited = visited | (1 << (2 * node))
            q.append((2 * node, time + 1))


def solution2():
    N, K = map(int, input().split())
    visited = [0] * 100001
    q = deque()
    visited[N] = 1
    q.append((N, 0))
    while q:
        node, time = q.popleft()
        if node == K:
            print(time)
            break

        if node - 1 >= 0 and visited[node - 1] == 0:
            visited[node - 1] = 1
            q.append((node - 1, time + 1))
        if node + 1 < len(visited) and visited[node + 1] == 0:
            visited[node + 1] = 1
            q.append((node + 1, time + 1))
        if 0 <= 2 * node < len(visited) and visited[2 * node] == 0:
            visited[2 * node] = 1
            q.append((2 * node, time + 1))


solution()