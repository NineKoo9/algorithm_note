def solution():
    N = int(input())
    arrays = list(map(int, input().split()))
    pre_end = int(1e9)
    # 가장 긴 증가하는 수열들을 나타내는 인덱스를 활용해볼까?
    dp = [0] * N
    dp[0] = 1
    if N == 1:
        return 1
    else:
        for i in range(1, N):
            for j in range(i):
                if arrays[i] > arrays[j]:
                    # 이런식으로 간다면 2차 dp 가 필요한가?
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    # 작은 경우는 어떻게 해야하지?
                    dp[i] = max(dp[i], 1)
    return max(dp)


# print(solution())
# 단순히 한단계 앞의 녀석의 포함여부를 비교하는 것으로는 무리가 있다.
# 그렇다면 그보다 더 앞의 녀석들을 비교해 나가야 할텐데? 그렇다면 이중 for문으로 확인을 해나가야할까? N이 1000인 이상 10만도 괜찮다.

def solution2():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(1)
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))

# 이 풀이는 뭐가 잘못된 것일까? 아... 첫 녀석부터 시작하는 것이 가장 긴 것이 아닐 수 있겠구나?
# 생각보다 반복문으로 풀어나갈때 까다롭네?
def solution3():
    N = int(input())
    A = list(map(int, input().split()))

    if N == 1:
        print(1)
        exit()
    dp = [0] * N
    dp[0] = 1
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
            else:
                dp[i] = max(dp[i], 1)

    print(max(dp))

def solution4():
    N = int(input())
    A = list(map(int, input().split()))
    
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))


solution4()