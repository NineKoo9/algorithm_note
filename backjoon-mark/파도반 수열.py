def solution():
    T = int(input())
    nums = [int(input()) for _ in range(T)]
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    for i in range(5, 101):
        dp[i] = dp[i - 1] + dp[i - 5]
    for num in nums:
        print(dp[num])

solution()