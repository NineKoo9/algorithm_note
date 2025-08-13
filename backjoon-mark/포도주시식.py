def solution():
    n = int(input()) # 10000개 까지 
    wines = [int(input()) for _ in range(n)] # 음이아닌 정수
    dp = [0] * n
    if n == 1:
        return wines[0]
    if n == 2:
        return wines[0] + wines[1]
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    for i in range(2, n):
        dp[i] = max(dp[i-2] + wines[i],
                    (dp[i-3] if i - 3 >= 0 else 0) + wines[i] + wines[i-1],
                    dp[i-1])
    return max(dp)

print(solution())
# 중간에 엄청 큰 텀으로 안먹어도 되는 것이잖아?
# 계단문제의 변형으로 봐도 되겠다.