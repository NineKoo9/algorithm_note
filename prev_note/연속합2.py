# 단순히 제일 작은 음수를 제거한다는게 의미가 있을까?
# 메모리 초과가 발생...
def solution():
    import copy

    n = int(input())
    arr = list(map(int, input().split()))
    dp = [
        [0] * n for _ in range(2)
    ]  # dp[0]은 특정원소 제거 안한 것 dp[1]은 제거한 것 (n,2)보다 (2,n)이 최대를구하는 식이 더 이쁠려나
    dp[0][0] = arr[0]  # 처음 녀석이 음수 일 수 있지만 반드시 하나는 선택해야 한다.
    # 이제부터 dp시작.
    if n == 1:
        print(arr[0])
    else:
        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
            dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])
        print(max(max(dp[0]), max(dp[1])))


# 계속 어디서 틀리는 것일까


def solution2():
    # 기본적으로 연속합은 비슷할 것이다.
    n = int(input())
    array = list(map(int, input().split()))
    # 먼저 완전 탐색을 위한 모든 음수를 다 적을까..?
    INF = int(1e9)
    dp = [[-INF] * n for _ in range(2)]
    dp[0][0] = array[0]
    if len(array) == 1:
        print(array[0])
    else:
        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1] + array[i], array[i])
            dp[1][i] = max(dp[1][i - 1] + array[i], dp[0][i - 1])
        print(max(max(dp[1]), max(dp[0])))
    pass

def solution3():
    n = int(input())
    numbers = list(map(int, input().split()))
    N = len(numbers)
    INF = int(1e9)
    dp = [[-INF] * N for _ in range(2)]
    if N == 1:
        print(numbers[0])
        return
    for i in range(N): # 지금처럼 N 으로 하면... dp[-1] 에 해당하는 부분이 어짜피 -INF 라서 계산결과가 올바르게 나오지만... 원래는 미리 초기화해두자
        dp[1][i] = max(dp[1][i - 1] + numbers[i], numbers[i]) # 전까지의 기록에 이어가거나 나부터 시작하거나
        dp[0][i] = max(dp[0][i - 1] + numbers[i], dp[1][i - 1] + numbers[i], dp[1][i - 1])

    print(dp[1])
    print(dp[0])
    print(max(max(dp[1]), max(dp[0])))

def solution4():
    N = int(input())
    A = list(map(int, input().split()))
    
    INF = int(1e9)
    # 약간 그런 고민이 생가는 군... i번째가 있는 경우 없는 경우로 갈것이냐 아니면 하나가 제거된 경우로 갈것이냐...
    # 그냥 후자로 가면 되는군
    dp = [[-INF for _ in range(N)], [A[i] for i in range(N)]] # dp[0][i]은 하나가 제거된 경우, dp[1][i]는 제거되지 않은 경우
    
    for i in range(1, N):
        dp[0][i] = max(dp[0][i - 1] + A[i], A[i], dp[1][i - 1]) # 제거된 경우라면? 앞부분에서 제거되었거나, i번째에서 제거되는 경우다.
        dp[1][i] = max(dp[1][i], dp[1][i - 1] + A[i]) # 제거되지 않은 경우라면 i-1도 제거되지 않은 경우여야 한다.
    print(max(max(dp[0]), max(dp[1])))

solution4()
