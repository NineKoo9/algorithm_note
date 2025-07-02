def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    # arr = 10 -4 3 1 5 6 -35 12 21 -1
    sums = [0] * n
    if n == 1:
        print(arr[0])
    else:
        sums[0] = arr[0]
        for i in range(1, n):
            sums[i] = max(sums[i - 1] + arr[i], arr[i - 1] + arr[i], arr[i])
        if arr[n - 1] > sums[n - 1]:
            sums[n - 1] = arr[n - 1]
        print(max(sums))


# 어쨋든 전체에서 최대값만 구하면 되잖아?
# 새로운 녀석이 들어왔을때 그녀석을 포함하는 최대값을 어떻게 구할까?
# 새로운 녀석이 들어 왔을때 그 녀석을 포함하는 최대값이라 생각해보자
# 그 전까지는 그 녀석을 포함하지 않는 최대값이 되겠지?
# n번째를 포함하년 녀석을 고려할 때, n-1 번째 와의 합만 고려하면 될까? n-2 + n-1 + n은?
# 이미 n-1을 고려할 때 n-1와의 합을 고려했고, 그 녀석은 전체 합보다 작다는 것이 확인 됨.
# 위의 식에서 한번 틀렸는데 뭐가 문제지?
# 새롭게 추가된 녀석이 그 하나만으로 매우 크다면 다른 녀석을 포함하는 경우로 할 필요가 없지...
# 그런데... 왜 arr[i-1] + arr[i] 이걸 빼도 가능한 걸까...
# 음 그건 당연한거지? 연속합이라면 바로 앞의 녀석도 최대값인데.. 그 녀석보다 현재값이 더 크다는 것은 바로앞녀석을 포함하는 연속값 + 본인을 더한 것보다
# 본인 자신이 더 크다는 말이잖아.


def solution2():
    n = int(input())
    seq = list(map(int, input().split()))
    max_sum = [0] * n
    max_sum[0] = seq[0]
    if len(seq) == 1:
        print(seq[0])
    else:
        for idx in range(1, n):
            max_sum[idx] = max(
                max_sum[idx - 1] + seq[idx], seq[idx]
            )  # 여기서 바로 직전까지의 최대썸은...
        print(max(max_sum))

def solution3():
    n = int(input())
    numbers = list(map(int, input().split()))
    N = int(len(numbers))
    INF = int(1e9)
    dp = [-INF] * N
    for i in range(N):
        dp[i] = max(dp[i-1] + numbers[i], numbers[i])
    print(max(dp))

def solution4():
    # 이 문제의 핵심은 어디서부터 연속인지를 확실하게 정하는 것이다. 그 수단을 위해 2차원 dp을 이용하는 것이다.
    n = int(input())
    nums = list(map(int, input().split()))
    INF = int(1e9)
    dp = [[-INF] * n for _ in range(2)]
    dp[0][0] = -INF
    dp[1][0] = nums[0]

    max_value = max(dp[0][0], dp[1][0])
    for i in range(1, n):
        dp[0][i] = nums[i]
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1]) + nums[i]
        max_value = max(max_value, dp[0][i], dp[1][i])

    print(max_value)

# 후... 머릿속으로 생각을 하고 어느 부분을 최적화를 할지 명확히 고려하자.
# 아무 생각없이 알고리즘 풀이만 외워되지 쓸데없이 이차원 dp나 만들고 있지....
# 핵심은 뭐냐? 완전탐색으로 가게된다면 i~N 일때 j~N까지 모든 경우를 다 고려해야한다. 하지만 이렇게 된다면 시간복잡도가 초과단다.
# 이때 생각을 조금 바꿔서 시작점 기준으로 오른쪽으로 늘려가는 것이 아닌 시작점 기준으로 왼쪽으로 점점 늘려간다고 생각해보자.
# . . . . . -
# . . . . - -
# . . . - - -
# . . - - - -
# 이런식으로 탐색한다 했을 때 i번째를 포함하는 여러가지의 연속합 중에서 어디가 가장 큰지 찾아야하는 문제다.
# 그렇다면 조금 더 생각해보자. i번째를 포함하는 가장 큰 연속합은 i-1번째의 가장 큰 연속합에서 A[i]를 더한것과 일치하지 않나?
# 그러니까 i-1번째까지의 연속합에서 단순히 A[i]를 더하기만 한것이기 때문에 여러 케이스가 있어도 결과자체는 달라지지 않을 것이란 것이다.
# 다만 1개만 선택하는 것도 가능하니 그 경우를 고려해주는 것이 맞다.

def solution5():
    N = int(input())
    A = list(map(int, input().split()))
    
    dp = [A[i] for i in range(N)]
    for i in range(1, N):
        dp[i] = max(dp[i], dp[i - 1] + A[i])
    print(max(dp))
    
    
solution5()
