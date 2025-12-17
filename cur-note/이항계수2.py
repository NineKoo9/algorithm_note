def solution():
    def factorial(n):
        if n == 0:
            return 1
        dp[n] = n * factorial(n - 1)
        return dp[n]
        
    N, K = map(int, input().split())
    dp = [1] * (N + 1)
    factorial(N)
    print((dp[N] // dp[K] // dp[N-K]) % 10007 )

def solution2():
    def factorial(n):
        # 이것을 구하는 것을 최적화하자?
        if n == 1 or n == 0:
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = n * factorial(n - 1)
        return dp[n]
    
    # nCk 을 구해야하는데
    n, k = map(int, input().split())
    # 어떻게 구할까? 팩토리얼 계산이 필요하다.
    dp = [-1] * (n + 1)
    ans = factorial(n) // (factorial(k) * factorial(n - k))
    print(ans % 10007)


solution2()