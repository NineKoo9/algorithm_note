def solution():
    N = int(input())
    P = list(map(int, input().split()))
    P.sort()
    total_time = 0
    result = 0
    for i in range(N):
        total_time += P[i]
        result += total_time
    print(result)

solution()