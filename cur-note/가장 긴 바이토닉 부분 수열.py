def solution():
    N = int(input())
    arrays = list(map(int, input().split()))
    reverse_arrays = arrays[::-1]
    i_dp = [0] * N
    d_dp = [0] * N
    i_dp[0] = 1
    d_dp[0] = 1
    
    for i in range(1, N):
        for j in range(i):
            if arrays[i] > arrays[j]:
                i_dp[i]  = max(i_dp[i], i_dp[j] + 1)
            else:
                i_dp[i] = max(i_dp[i], 1)
            if reverse_arrays[i] > reverse_arrays[j]:
                d_dp[i] = max(d_dp[i], d_dp[j] + 1)
            else:
                d_dp[i] = max(d_dp[i], 1)
    print(i_dp)
    print(d_dp[::-1])
    print(max((map(lambda t:t[0] + t[1], zip(i_dp, d_dp[::-1]))))-1)

def solution2():
    N = int(input())
    A = list(map(int, input().split()))
    # 바이토닉에서 사장 긴 것을 할려면 특정 지점까지 가장 긴 증가하는 수열이 되어야 하고... 반대쪽에서 가장 긴 증가하는 수열이 되면 되겠네?
    increase_dp = [1] * N
    reverse_increase_dp = [1] * N

    if N == 1:
        print(1)
        return
    # 먼저 정방향 증가.
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)
    # 이제 역방향 증가
    for i in reversed(range(N - 1)):
        for j in reversed(range(i, N)):
            if A[i] > A[j]:
                reverse_increase_dp[i] = max(reverse_increase_dp[i], reverse_increase_dp[j] + 1)
    print(max(list(map(lambda t: sum(t) - 1, zip(increase_dp, reverse_increase_dp)))))

def solution3():
    N = int(input())
    A = list(map(int, input().split()))
    
    # 여기서부터 가장 긴 바이토닉 부분 수열을 구해야한다.
    increase_dp = [1] * N
    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)
            
    decrease_dp = [1] * N
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, i - 1, -1):
            if A[j] < A[i]:
                decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)
    
    ans = 0
    for i, j in zip(increase_dp, decrease_dp):
        ans = max(ans, i + j - 1)
    print(ans)

solution3()