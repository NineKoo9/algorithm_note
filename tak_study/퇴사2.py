import sys

sys.setrecursionlimit(1600000)
input = sys.stdin.readline

def solution():
    # 이것이 바로 탑다운이다.
    def recur(cur):
        # recur(4) 일때 어떤 값을 반환할지 생각하자.
        if cur == N:
            # 이때 딱 완료되는데 맥스 값을 갱신해야지?
            # 근데... 내가 지금 할려는 것은.. 시간복잡도가 너무 크다.
            # 그래서 최적화를 해야하고
            return 0 # 자 한번 생각해보자. recur(0) 일때 가져갈 수 있는 이득은? 0
        if cur > N:
            # 이 경우 선택이 불가능하다.
            return -int(1e9)
        if dp[cur] != -1:
            return dp[cur]

        dp[cur] = max(recur(cur + meetings[cur][0]) + meetings[cur][1], recur(cur + 1))
        return dp[cur]

    N = int(input())
    meetings = [list(map(int, input().split())) for _ in range(N)]
    dp = [-1] * N  # 결국 시간복잡도는 dp의 테이블을 모두 한번씩 방문하는 정도가 될것이고... 곱하기 내부 연산정도

    print(recur(0))

# gpt가 짜준 최적화한 코드...
def solution2():
    N = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(N)]
    # dp 배열을 N+1 크기로 만들어 경계 처리를 간단히 함.
    dp = [0] * (N + 1)

    # 뒤에서부터 반복하여 각 날짜에 대해 최적의 이득을 계산
    for i in range(N - 1, -1, -1):
        time, profit = meetings[i]
        if i + time <= N:
            dp[i] = max(profit + dp[i + time], dp[i + 1])
        else:
            dp[i] = dp[i + 1]
    print(dp[0])

# 이번 풀이는 바텀업 풀이다.
def solution3():
    N = int(input())
    meetings = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (N + 1)  # 어쨋든 처음에 얻을 수 있는 수익은 0이다.

    for i in range(N - 1, -1, -1):
        # i날짜에 얻을 수 있는 금액은?
        t, p = meetings[i]
        if i + t <= N:
            dp[i] = max(dp[i + t] + p, dp[i + 1])  # 선택한 경우와 선택하지 않은 경우를 비교한다.
        else:
            dp[i] = dp[i + 1]

    print(dp[0])

solution3()