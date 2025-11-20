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

def solution2():
    def dfs(start_color, prev_color, curr_house_idx):

        # 마지막 집까지 도달한 경우
        if curr_house_idx == N:
            return 0
        
        if dp[start_color][prev_color][curr_house_idx] != -1:
            return dp[start_color][prev_color][curr_house_idx]
        
        cost = int(1e9)

        for curr_color, cur_house_cost in enumerate(house_costs[curr_house_idx]):
            if prev_color == curr_color:
                continue
            
            # 만약 마지막 집이라면, 첫번째 집과 같으면 안된다.
            if curr_house_idx == N - 1 and start_color == curr_color:
                continue

            next_cost = dfs(start_color, curr_color, curr_house_idx + 1)
            cost = min(cost, cur_house_cost + next_cost)
        dp[start_color][prev_color][curr_house_idx] = cost
        return cost

    N = int(input())
    house_costs = [list(map(int, input().split())) for _ in range(N)]
    INF = int(1e9)

    # dp[start_color][prev_color][curr_house_idx] 의 최소를 저장한다.
    dp = [[[-1 for _ in range(N)] for _ in range(3)] for _ in range(3)]
    
    answer = INF
    for start_color in range(3):
        answer = min(answer, house_costs[0][start_color] + dfs(start_color, start_color, 1))

    print(answer)

solution2()