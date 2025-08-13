# import sys
#
# N = int(sys.stdin.readline())
# INF = int(1e9)
# matrix_lst = [tuple(map(int, sys.stdin.readline().split())) for i in range(N)]  # 여기에 메트릭스 번호의 범위에 해당하는 (행, 열)값을 저장할 것이다.
# matrix_info = [[(0, 0)] * N for _ in range(N)]
# for idx, matrix in enumerate(matrix_lst):
#     row, col = matrix
#     matrix_info[idx][idx] = (row, col)
#
# dp = [[INF] * N for _ in range(N)]
# # 본인에서 본인까지의 연산의 최소값은 0이니까 먼저 초기화 해준다.
# for i in range(N):
#     dp[i][i] = 0
#
# for length in range(1, N):  # 메트릭스 길이에 해당하는 것이다.
#     for i in range(N - length):
#         j = i + length
#         for m in range(i, j):  # m의 값은 최대 j - 1 을 가질 것이다.
#             row1, col1 = matrix_info[i][m]
#             _, col2 = matrix_info[m + 1][j]
#             tmp = dp[i][m] + dp[m + 1][j] + (row1 * col1 * col2)
#             if dp[i][j] > tmp:
#                 dp[i][j] = tmp
#                 matrix_info[i][j] = (row1, col2)
# print(dp[0][N - 1])
from zmq.backend import second


# 시간초과가 발생하였다...
# matrix info을 해시로서 저장했는데... 리스트로 저장하니까 속도가 더 빨라졌다.

def solution2():
    N = int(input())
    M = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[int(1e9)] * N for _ in range(N)]
    matrix = [[(0, 0)] * N for _ in range(N)]

    for i, m in enumerate(M):
        r, c = m
        matrix[i][i] = (r, c)
        dp[i][i] = 0

    for step in range(1, N):
        for i in range(N - step):
            j = i + step
            for m in range(i, j):
                matrix1 = matrix[i][m]
                matrix2 = matrix[m + 1][j]
                cost = matrix1[0] * matrix1[1] * matrix2[1]
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j] + cost)
                matrix[i][j] = (matrix1[0], matrix2[1])
    print(dp[0][N - 1])

def solution3():
    N = int(input())
    matrix_lst = [tuple(map(int, input().split())) for _ in range(N)]

    INF = int(1e9)
    dp = [[(INF, (0, 0))] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = (0, matrix_lst[i])

    for step in range(1, N):
        for i in range(N - step):
            j = i + step
            for k in range(i, j):
                first_cost, first_matrix = dp[i][k]
                second_cost, second_matrix = dp[k + 1][j]
                cur_cost, _ = dp[i][j]
                a, b, c = first_matrix[0], first_matrix[1], second_matrix[1]
                if cur_cost > first_cost + second_cost + a * b * c:
                    dp[i][j] = (first_cost + second_cost + a * b * c, (a, c))

    print(dp[0][-1][0])

solution3()