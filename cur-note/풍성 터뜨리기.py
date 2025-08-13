def solution():
    from collections import deque
    
    N = int(input())
    ballons = deque([(idx, num) for idx, num in enumerate(map(int, input().split()), start = 1)])
    answer = []
    while ballons:
        ballon_num, dist = ballons.popleft()
        answer.append(ballon_num)
        ballons.rotate(-(dist - 1) if dist > 0 else -dist)
    print(" ".join(map(str, answer)))
    
solution()