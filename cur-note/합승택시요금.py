def solution(n, s, a, b, fares):  # n지점의 갯수, s 출발지점, a의 집, b의 집, fares 요금
    # 구하고자 하는 것은 두 사람이 모두 귀가하는 데 소요되는 예상 최저 택시요금!
    # 자 반대로 한번 생각해보자. A와 B 두 지점에서 가장 비용이 작은 지점을 구할 수 있을까?
    # 일단 플로이드 워샬도 사용가능하다. 최소 비용이니까
    # 각 경우마다 최소비용을 갱신해나가면 될것같다.
    INF = int(1e9)
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    min_answer = INF
    for start, end, fare in fares:
        dp[start][end] = fare
        dp[end][start] = fare
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    dp[i][j] = 0
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        # k지점을 경유하는 경우를 모두 갱신했으니 k지점까지 함께 탄 경우 최소비용을 계산해보자.
        # --> 이 코드는 잘못되었다.
        #(1, 5, 35), (1, 6, 35), (1, 2, 100), (2, 5, 10), (2, 6, 10), (1, 4, 5), (4, 2, 5) 이 케이스에서 틀린다.
        min_answer = min(min_answer,
                         dp[s][k] + dp[k][a] + dp[k][b],
                         dp[s][a] + dp[s][b])
    return min_answer

def solution1(n, s, a, b, fares):  # n지점의 갯수, s 출발지점, a의 집, b의 집, fares 요금
    # 구하고자 하는 것은 두 사람이 모두 귀가하는 데 소요되는 예상 최저 택시요금!
    # 자 반대로 한번 생각해보자. A와 B 두 지점에서 가장 비용이 작은 지점을 구할 수 있을까?
    # 일단 플로이드 워샬도 사용가능하다. 최소 비용이니까
    # 각 경우마다 최소비용을 갱신해나가면 될것같다.
    INF = int(1e9)
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    for start, end, fare in fares:
        dp[start][end] = fare
        dp[end][start] = fare
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    dp[i][j] = 0
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return min([dp[s][k] + dp[k][a] + dp[k][b] for k in range(1, n + 1)])
        