from collections import deque

def solution():
    N, K = map(int, input().split())
    S = list(map(int, input().split()))
    
    q = deque()
    odd_count = 0
    ans = 0
    for i in range(N):
        if S[i] % 2 != 0:
            odd_count += 1
        q.append(S[i])
        while odd_count > K and q:
            first = q.popleft()
            if first % 2 != 0:
                odd_count-= 1
        ans = max(ans, len(q) - odd_count)
    print(ans)

def solution2():
    N, K = map(int, input().split())
    S = list(map(int, input().split()))
    
    start = 0
    odd_count = 0
    ans = 0
    for end in range(N):
        if S[end] % 2 != 0:
            odd_count += 1
        while odd_count > K and start <= end:
            first = S[start]
            if first % 2 != 0:
                odd_count -= 1
            start += 1
        ans = max(ans, end - start + 1 - odd_count)
    print(ans)
    
solution2()