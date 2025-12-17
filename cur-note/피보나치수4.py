def solution():
    import sys
    
    sys.setrecursionlimit(100000)
    def fibo(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if dp[n] != -1:
                return dp[n]
            dp[n] = fibo(n - 1) + fibo(n - 2)
            return dp[n]    
    
    N = int(input())
    dp = [-1 for _ in range(N + 1)]
    print(fibo(N))

solution()
