def solution():
    N, M = map(int, input().split())  # N개의 앱이 활성화, M 이상의 메모리를 확보해야함
    active_app_memory = list(map(int, input().split()))
    de_active_cost = list(map(int, input().split()))
    INF = int(1e9)
    dp = [[0] * 10001 for _ in range(N)]
    min_cost = INF

    for i in range(N):
        for cost in range(10001):
            require_cost, memory = de_active_cost[i], active_app_memory[i]
            dp[i][cost] = max(dp[i - 1][cost],
                              dp[i - 1][cost - require_cost] + memory if cost - require_cost >= 0 else 0)
            if dp[i][cost] >= M:
                min_cost = min(min_cost, cost)
    print(min_cost)

def solution2():
    N, M = map(int, input().split())
    used_memories = list(map(int, input().split()))
    de_activate_costs = list(map(int, input().split()))
    max_cost = N * max(de_activate_costs) + 1
    dp = [[0] * N for _ in range(max_cost)]
    for cost in range(max_cost):
        for i in range(N):
            if cost < de_activate_costs[i]:
                dp[cost][i] = max(dp[cost][i], dp[cost][i - 1] if i - 1 >= 0 else 0)
            else:  # cost >= de_activate_costs[i]:
                dp[cost][i] = max(dp[cost][i - 1], used_memories[i] + (dp[cost - de_activate_costs[i]][i - 1] if i - 1 >= 0 else 0))
            if dp[cost][i] >= M:
                print(cost)
                exit()


def solution3():
    N, M = map(int, input().split())
    used_memories = list(map(int, input().split()))
    de_activate_costs = list(map(int, input().split()))

    # Maximum cost to be considered
    max_cost = sum(de_activate_costs)

    # DP array to track maximum memory that can be freed for a given cost
    dp = [0] * (max_cost + 1)

    # Fill the dp array
    for i in range(N):
        cost = de_activate_costs[i]
        memory = used_memories[i]
        for current_cost in range(max_cost, cost - 1, -1):
            dp[current_cost] = max(dp[current_cost], dp[current_cost - cost] + memory)

    # Find the minimum cost to achieve at least M memory
    for cost in range(max_cost + 1):
        if dp[cost] >= M:
            print(cost)
            break

# 그냥 풀었을 땐 틀렸는데 여기서 예외 케이스를 어떻게 따져볼까?
# 인덱스 조차 어떤 값을 나타낼 수 있다는 것은 매우 중요하다.
# 어우... 초기에 max_cost을 막연히 100으로 잡았다가 문제를 못풀었고...
# if 문 처리도 제대로 못해서 인덱스로 이상한게 들어갔네
def solution4():
    N, M = map(int, input().split())

    used_memory = list(map(int, input().split()))
    deactivate_cost = list(map(int, input().split()))
    max_cost = sum(deactivate_cost) + 1

    dp = [[0] * N for _ in range(max_cost)]
    min_cost = int(1e9)
    for cost in range(max_cost):
        for i in range(N):
            if cost >= deactivate_cost[i]:
                dp[cost][i] = max(dp[cost][i - 1] if i - 1 >= 0 else 0,
                                  used_memory[i] + (dp[cost - deactivate_cost[i]][i - 1] if i - 1 >= 0 else 0))
            else: # 만약 i번째를 고려할 수 없다면?
                dp[cost][i] = max(dp[cost][i], dp[cost][i - 1] if i - 1 >= 0 else 0)

            # 자 이제 확부한 메모리를 비교해야 하는데
            if dp[cost][i] >= M:
                min_cost = min(min_cost, cost)

    print(min_cost)


solution4()
# 냅색문제랑 비슷한거 같은데?
# 문제를 다르게 생각하면 최소 M이상의 메모리를 가져야할때, 최소의 비용을 구하여라!
# 뭔가 이상하다... 최소비용 그거 만들 수 있는 것이어야 하잖아?
# 최소 min_cost 에서 같은 i 번째 라인에서 제일 작은 cost 가 들어가겠지? 그리고 그곳에서 M이상 이였다면 변경이 일어났다는 것이니까
# 변경이 일어났다는 것은 메모리 확보가 가능한 케이스다?
# dp 값으로 최대 확보할 수 있는 메모리가 들어가는 문제로 바꾸는 것은 그래프를 그려보기전까지 상상하기가 쉽지않다.
# 그치만 이런게 가능하다는 것을 알게되었고 언젠가 코테에서 본다면 떠올려보자
