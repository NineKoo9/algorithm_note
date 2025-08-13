
min_value = int(1e9)
def solution():
    global min_value

    def recur(cur, prev_selected, cost):
        global min_value
        print(cur, prev_selected, cost)

        if cur == N:
            min_value = min(min_value, cost)
            return

        # 빨강 선택
        if prev_selected != 0:
            recur(cur + 1, 0, cost + costs[cur][0])

        # 초록 선택
        if prev_selected != 1:
            recur(cur + 1, 1, cost + costs[cur][1])

        # 블루 선택
        if prev_selected != 2:
            recur(cur + 1, 2, cost + costs[cur][2])

    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    recur(0, 0, 0)
    recur(0, 1, 0)
    recur(0, 2, 0)
    print(min_value)

# 위의 풀이는 완전탐색이고 시간초과가 걸릴것이다. 위의 코드를 반환형으로 바꿔보자.
def solution2():
    def recur(cur, prev_selected):
        if cur == N:
            return 0

        # 빨강 선택
        r, g, b = int(1e9), int(1e9), int(1e9)
        if prev_selected != 0:
            r = recur(cur + 1, 0) + costs[cur][0]
        # 초록 선택
        if prev_selected != 1:
            g = recur(cur + 1, 1) + costs[cur][1]
        # 블루 선택
        if prev_selected != 2:
            b = recur(cur + 1, 2) + costs[cur][2]

        return min(r, g, b)



    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    print(recur(0, -1))

# 여전히 시간복잡도는 높다. dp를 적용해보자.
def solution3():
    def recur(cur, prev_selected):
        if cur == N:
            return 0

        if dp[cur][prev_selected] != -1:
            return dp[cur][prev_selected]

        # 빨강 선택
        r, g, b = int(1e9), int(1e9), int(1e9)
        if prev_selected != 0:
            r = recur(cur + 1, 0) + costs[cur][0]
        # 초록 선택
        if prev_selected != 1:
            g = recur(cur + 1, 1) + costs[cur][1]
        # 블루 선택
        if prev_selected != 2:
            b = recur(cur + 1, 2) + costs[cur][2]

        dp[cur][prev_selected] = min(r, g, b)
        return dp[cur][prev_selected]



    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * 3 for _ in range(N)]
    print(recur(0, -1))

solution3()