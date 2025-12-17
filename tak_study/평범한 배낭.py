max_value = 0
def solution():
    global max_value
    def recur(cur, weight, value):
        global max_value
        if cur == N:
            if weight <= K:
                max_value = max(max_value, value)
            return

        # 선택하는 경우
        w, v = objects[cur]
        recur(cur + 1, weight + w, value + v)

        # 선택하지 않는 경우
        recur(cur + 1, weight, value)

    N, K = map(int, input().split())
    objects = [list(map(int, input().split())) for _ in range(N)]

    recur(0, 0, 0)

    print(max_value)

def solution2():
    def recur(cur, weight):
        if weight > K:
            return -int(1e9)
        if cur == N:
            return 0

        if dp[cur][weight] != -1:
            return dp[cur][weight]

        # 선택하는 경우
        w, v = objects[cur]
        select_result = recur(cur + 1, weight + w) + v

        # 선택하지 않는 경우
        un_select_result = recur(cur + 1, weight)
        dp[cur][weight] = max(select_result, un_select_result)
        return dp[cur][weight]

    N, K = map(int, input().split())
    objects = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * 100001 for _ in range(N)]

    print(recur(0, 0))

solution2()