def solution():
    for _ in range(int(input())):
        K = int(input())
        files = list(map(int, input().split()))
        # 연속된 합을 구하는데... 가장 최소의 비용이 되도록 합해야한다.
        # 애초에 이 문제 완탐을 생각하는 것부터 쉽지가 않다. 어떻게 완탐을 고려할까 그 자체가 어렵네
        prefix_sum = [0] * (K + 1)
        for i in range(1, K + 1):
            prefix_sum[i] = prefix_sum[i - 1] + files[i - 1]
        
        INF = int(1e9)
        dp = [[INF] * K for _ in range(K)]
        
        # 우선 길이가 1인 경우 비용은 0이다.
        for i in range(K):
            dp[i][i] = 0
        
        # 길이가 2이상인 경우
        for l in range(2, K + 1):
            for i in range(K - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], prefix_sum[k + 1] - prefix_sum[i] + dp[i][k] \
                                                + prefix_sum[j + 1] - prefix_sum[k + 1] + dp[k + 1][j])
        print(dp[0][-1])

solution()