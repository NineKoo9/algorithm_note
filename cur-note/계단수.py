def solution():
    N = int(input())

    dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N + 1)]

    # 길이가 1이고 가장 오른쪽이 1~9인 i인 경우
    for i in range(1, 10):
        dp[1][i][1 << i] = 1
    #
    # 길이가 size이고 가장 오른쪽이 0~9인 i인 경우
    for size in range(2, N + 1):
        for i in range(10):
            # 기존의 state는 뭐야? 그러니까 size가 1 작은 경우지 거기에 i - 1 i + 1인 녀석의 state 그렇다면 이것을 기록해나가야하나? 아... 이 경우가 너무나 다양하다.
            for state in range(1024):
                if i == 0:
                    # 기존의 state는 무엇이냐?
                    # 덮어쓰기(=)와 누적하기(+=)를 혼동
                    dp[size][i][state | (1 << i)] += dp[size - 1][1][state]
                elif i == 9:
                    dp[size][i][state | (1 << i)] += dp[size - 1][8][state]
                elif size == 2 and i == 1:
                    dp[size][i][state | (1 << i)] += dp[size - 1][i + 1][state]
                else:
                    dp[size][i][state | (1 << i)] += (dp[size - 1][i - 1][state] + dp[size - 1][i + 1][state])

    print(sum(dp[N][i][(1 << 10) - 1] for i in range(10)) % int(1e9))

solution()