def solution():
    from collections import deque
    N, K = map(int, input().split())
    
    q = deque([i for i in range(1, N+1)])
    answer = []
    while q:
        q.rotate(-(K-1))
        answer.append(q.popleft())
    
    print("<" + ", ".join(map(str, answer)) + ">")


solution()
N, K = map(int, input())
scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[K-1])