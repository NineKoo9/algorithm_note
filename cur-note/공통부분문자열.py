def solution():
    A = input()
    B = input()

    a_len = len(A)
    b_len = len(B)

    dp = [[0] * b_len for _ in range(a_len)]

    max_length = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                dp[i][j] = (dp[i - 1][j - 1] + 1) if i != 0 and j != 0 else 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
    print(max_length)

solution()