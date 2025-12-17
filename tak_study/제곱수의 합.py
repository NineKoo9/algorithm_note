def solution():
    import math
        
    N = int(input())
    INF = int(1e9)
    dp = [INF] * (N + 1)
    dp[0] = 0
    for n in range(1, N + 1):
        for k in range(int(math.sqrt(n)) + 1):
            if n - k**2 < 0:
                continue
            if n - k**2 == 0:
                dp[n] = 1
            else:
                dp[n] = min(dp[n], dp[n - k**2] + 1)
    print(dp[N])
        
    
solution()