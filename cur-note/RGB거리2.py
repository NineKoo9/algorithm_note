def solution():
    N = int(input())
    costs = [tuple(map(int, input().split())) for _ in range(N)]

    INF = int(1e9)
    dp = {ch: [[0, 0, 0] for _ in range(N)] for ch in ["r", "g", "b"]}
    dp["r"][0] = [costs[0][0], INF, INF]
    dp["g"][0] = [INF, costs[0][1], INF]
    dp["b"][0] = [INF, INF, costs[0][2]]
    for ch in ["r", "g", "b"]:
        for j in range(1, N):
            dp[ch][j][0] = min(dp[ch][j - 1][1], dp[ch][j - 1][2]) + costs[j][0]
            dp[ch][j][1] = min(dp[ch][j - 1][0], dp[ch][j - 1][2]) + costs[j][1]
            dp[ch][j][2] = min(dp[ch][j - 1][0], dp[ch][j - 1][1]) + costs[j][2]

    min_value = INF
    for i, ch in enumerate(["r", "g", "b"]):
        for j in range(3):
            if i != j:
                min_value = min(min_value, dp[ch][-1][j])
    print(min_value)


solution()