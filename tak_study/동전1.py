import sys

sys.setrecursionlimit(100000)
# 이 코드 자바로 고치니 완전히 동작한다. 드디어... 속시원하다
def solution():
    def recur(cur, value):
        if value == K:
            return 1
        if value > K:
            return 0
        if cur == N:
            return 0

        if dp[cur][value]:
            return dp[cur][value]
        count = 0
        # 현재 코인을 뽑거나
        count += recur(cur, value + coins[cur])
        # 현재 코인을 뽑지 않거나.
        count += recur(cur + 1, value)
        dp[cur][value] = count
        return count

    # 이 문제.. 중복 조합으로 생각할 수 있겠다.
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    dp = [[0] * K for _ in range(N)]
    print(recur(0, 0))

solution()