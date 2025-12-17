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

def solution2():
    def dfs(idx, num, cur_state):
        # 마지막에 도달했고
        if idx == N - 1:
            # 모든 수들이 나타났다면 1
            if cur_state == (1 << 10) - 1:
                return 1
            # 그게 아니라면 0
            else:
                return 0
        
        if dp[idx][num][cur_state] != -1:
            return dp[idx][num][cur_state]
        
        count = 0
        for diff in [1, -1]:
            next_num = num + diff
            if not (0 <= next_num < 10):
                continue
            count += dfs(idx + 1, next_num, cur_state | 1 << next_num)
        dp[idx][num][cur_state] = count
        return dp[idx][num][cur_state]


    N = int(input())

    # dp[idx][n][state] 이면 idx에 n이 있고 지금까지 방문항 state라면 그 뒤로 방문해야할 지점들은 결정되어 있다.
    dp = [[[-1 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N)]
    for first_num in range(1, 10):
        dfs(0, first_num, 1 << first_num)

    # 이렇게 되면 1을 처음 방문, 9을 처음 방문... 이 경우에 대한 수를 모두 더하는 것이 되겠군
    print(sum(dp[0][n][1 << n] for n in range(1, 10) if dp[0][n][1 << n] != -1) % 1000000000)

solution2()