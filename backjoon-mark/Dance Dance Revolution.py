import sys

sys.setrecursionlimit(100000)

min_cost = int(1e9)

# 이 풀이는 시간복잡도가 2^n이다.
def solution():
    global min_cost

    def dfs(foot, step_idx, cost):
        global min_cost

        if steps[step_idx] == 0:
            # 마지막까지 스탭을 밟았다면.. 비용을 고려해야지
            min_cost = min(min_cost, cost)
            return

        # 자 여기서 오른쪽발이 움직이냐 왼쪽발이 움직이냐에 따라서 달라지는데..
        # i번째 발이 움직인다고 생각하자
        for i in range(2):
            if foot[i] == 0:
                n_cost = cost + 2
            elif foot[i] == steps[step_idx]:
                n_cost = cost + 1
            elif foot[i] % 2 == steps[step_idx] % 2:
                n_cost = cost + 4
            else:
                n_cost = cost + 3
            next_foot = foot.copy()
            next_foot[i] = steps[step_idx]
            dfs(next_foot, step_idx + 1, n_cost)

    steps = list(map(int, input().split()))

    dfs([0, 0], 0, 0)

    print(min_cost)


# 단순히 prev1, prev2 을 기준으로 평가하기에는... 훨씬 앞선 녀석을 밟고있는 상태에서 다른 발로 계속 새롭게 밟아 나갈 수 있다.
def solution2():
    def get_next_cost(next_point, cur_point):
        if cur_point == 0:
            cost = 2
        elif next_point == cur_point:
            cost = 1
        elif next_point % 2 == cur_point % 2:
            cost = 4
        else:
            cost = 3
        return cost

    steps = list(map(int, input().split()))
    steps.pop()

    INF = int(1e9)
    dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(len(steps))]

    dp[0][steps[0]][0] = 2
    dp[0][0][steps[0]] = 2

    for idx in range(1, len(steps)):
        for i in range(5):
            for j in range(5):
                next_step = steps[idx]

                # 이것은 i번에 있는 왼쪽 발을 다음 녀석으로 밟을 때를 구하는 것이다.
                dp[idx][next_step][j] = min(dp[idx][next_step][j], dp[idx - 1][i][j] + get_next_cost(next_step, i))

                # 이것은 j의 위치에 있는 오른쪽 발을 다음 녀석으로 밟는 경우를 따지는 것이다.
                dp[idx][i][next_step] = min(dp[idx][i][next_step], dp[idx - 1][i][j] + get_next_cost(next_step, j))

    min_value = int(1e9)
    for i in range(5):
        for j in range(5):
            min_value = min(min_value, dp[-1][i][j])

    print(min_value)

solution2()