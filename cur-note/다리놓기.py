def solution():
    def factorial(n):
        if n == 1:
            return 1
        dp[n] = n * factorial(n-1)
        return dp[n]
    
    def bridge_count(w, e):
        # 정확하게는 e개의 점중에 w개를 골라서 줄을 새우는 것이고 w에는 순서가 존재한다...
        return dp[e] // dp[e - w] // dp[w]
        
    
    T = int(input())
    cases = [tuple(map(int, input().split())) for _ in range(T)]
    dp = [1] * (30)
    factorial(29)
    
    
    for case in cases:
        print(bridge_count(*case))

solution()