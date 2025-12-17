# 이 코드는 메모리 초과가 나타난다.
def solution():
    def recur(cur, w_remain ,h_remain, prev_2, prev_1):
        if cur == total:
            if w_remain == 0 and h_remain == 0:
                return 1
            return 0

        if dp[cur][w_remain][h_remain][prev_2][prev_1] != -1:
            return dp[cur][w_remain][h_remain][prev_2][prev_1]


        # w을 선택 근데 연속적인거 안됨.
        count = 0
        if w_remain > 0:
            if cur <= 1 or (not (prev_2 == "w" and prev_1 == "h")):  # 어짜피 여기서 검증하잖아?
                count += recur(cur + 1, w_remain - 1, h_remain, prev_1, "w")
        # h을 선택
        if h_remain > 0 :
            if cur <= 1 or (not (prev_2 == "h" and prev_1 == "w")):
                selected[cur] = "h"
                count += recur(cur + 1, w_remain, h_remain - 1, prev_1, "h")
        dp[cur][w_remain][h_remain][prev_2][prev_1] = count
        return count

    W, H = map(int, input().split())
    w, h = W - 1, H - 1
    total = w + h
    selected = [""] * total
    dp = [[[{ch: {ch: -1 for ch in ["", "h", "w"]} for ch in ["", "h", "w"]} for _ in range(h + 1)] for _ in range(w + 1)] for _ in range(total)]
    print(recur(0, w, h, "", "") % 100000)


# cur을 지우는 것으로 훨씬 최적화를 진행했다...
def solution2():  # 지금부터 w:1, h:2 로 하겠다.
    def recur(w_count ,h_count, prev_2, prev_1):
        if w_count + h_count == total:
            return 1

        if dp[w_count][h_count][prev_2][prev_1] != -1:
            return dp[w_count][h_count][prev_2][prev_1]

        count = 0
        # w을 선택 근데 연속적인거 안됨.
        if w_count < w and not (prev_2 == 1 and prev_1 == 2):
            count += recur(w_count + 1, h_count, prev_1, 1)
        # h을 선택
        if h_count < h and not (prev_2 == 2 and prev_1 == 1):
            count += recur(w_count, h_count + 1, prev_1, 2)
        dp[w_count][h_count][prev_2][prev_1] = count % 100000
        return dp[w_count][h_count][prev_2][prev_1]

    W, H = map(int, input().split())
    w, h = W - 1, H - 1
    total = w + h
    dp = [[[[-1 for _ in range(3)] for _ in range(3)] for _ in range(h + 1)] for _ in range(w + 1)]
    print(recur(0, 0, 0, 0))
solution2()