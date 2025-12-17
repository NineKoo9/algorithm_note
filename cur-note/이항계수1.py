def solution():
    def factorial(n):
        if n == 0:
            return 1
        dp[n] = n * factorial(n - 1)
        return dp[n]
        
    N, K = map(int, input().split())
    dp = [1] * (N + 1)
    factorial(N)
    print(dp[N] // dp[K] // dp[N-K])

solution()