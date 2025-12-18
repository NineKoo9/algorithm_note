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

def solution2():
    A = input()
    B = input()

    # 문자열 일치를 확인하기 이전에 가장 먼저 문자열 하나하나가 일치하는 것을 확인해야한다.
    # 그리고 문자열 하나가 일치한다면? 뒤이어서 연속된 녀석들이 일치하는 지 확인해야한다.
    # 만약 일치하지 않는다면? 다시 그냥 넘어가야한다.

    max_length = 0
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                # 한칸 증가시켰으니 dp[-1]이것은 그냥 제일 뒤의 빈칸 값을 읽어올 것이다.
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])

    print(max_length)

solution2()