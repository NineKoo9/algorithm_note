import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 위의 코드는 탑다운인데... 메모리 초과가 발생한다.
def solution():
    def recur(l, r):
        if l == r:
            return 0
        if l + 1 == r and nums[l] == nums[r]:
            return 0

        if dp[l][r] != -1:
            return dp[l][r]

        a, b = INF, INF
        # 같은 경우
        if nums[l] == nums[r]:
            dp[l][r] = recur(l + 1, r - 1)
        else:
            dp[l][r] = min(recur(l + 1, r), recur(l, r - 1)) + 1
        return dp[l][r]

    N = int(input())
    INF = int(1e9)
    nums = list(map(int, input().split()))
    dp = [[-1] * N for _ in range(N)]
    print(recur(0, N - 1))

# 위의 코드를 바텀업으로 변경해보자.
def solution2():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]

    for length in range(2, N + 1): # 생각해보니 길이가 1이라면 어짜피 값은 0이구나
        for l in range(0, N - length + 1):
            r = l + length - 1
            if nums[l] == nums[r]:
                dp[l][r] = dp[l + 1][r - 1] if l + 1 <= r - 1 else 0
            else:
                dp[l][r] = min(dp[l + 1][r], dp[l][r - 1]) + 1
    print(dp[l][r])
solution2()