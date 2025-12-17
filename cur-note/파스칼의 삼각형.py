def solution():
    def pascal_triangle(n, k):
        if n == 1 or k == 1 or n == k:
            return 1
        
        if dp[n][k] != -1:
            return dp[n][k]
        
        dp[n][k] = pascal_triangle(n - 1, k - 1) + pascal_triangle(n - 1, k)
        return dp[n][k]
    N, K = map(int, input().split())
    dp = [[-1] * (K + 1) for _ in range(N + 1)]
    print(pascal_triangle(N, K))
    
solution()