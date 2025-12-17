def solution():
    N = int(input())
    INF = int(1e9)
    dp = [INF] * (N + 1)
    path = [[] for _ in range(N + 1)]
    dp[1] = 1
    path[1] = [1]
    if N == 1:
        print(0)
        print(1)
    else:
        for n in range(2, N + 1):
            prev_n = n - 1
            if n % 2 == 0 and dp[prev_n] > dp[n // 2]:
                prev_n = n // 2
            if n % 3 == 0 and dp[prev_n] > dp[n // 3]:
                prev_n = n // 3
            prev_path = path[prev_n].copy()
            prev_path.append(n)
            dp[n] = len(prev_path)
            path[n] = prev_path

        print(dp[N] - 1)
        print(*path[N][::-1])

solution()