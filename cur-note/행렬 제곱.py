
# def calc_matrix(a, b):
#     R = [[0] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             r = 0
#             for k in range(N):
#                 r += ((a[i][k] % 1000) * (b[k][j] % 1000)) % 1000
#             R[i][j] = r % 1000
#     return R

# def calc(A, B): # 여기서 A는 matrix 이고 B는 숫자이다.
#     if B == 1:
#         for i in range(N):
#             for j in range(N):
#                 A[i][j] %= 1000
#         return A
#     elif B == 2:
#         return calc_matrix(A, A)
#     else:
#         if B % 2 == 0:
#             return calc(calc(A, B//2), 2)
#         else: # 만약 B가 홀수라면? 
#             return calc_matrix(calc(calc(A, B // 2), 2), calc(A, 1)) # 아 여기 A의 크기에 따라 다르지...

# N, B = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# R = calc(A, B)
# for row in R:
#     print(*row)

# B가 3인 경우... calc(A, 1)이 들어가는 구나..?

def soluiton():
    def calc_matrix(matrix1, matrix2):
        N = len(matrix1)
        result = [[0] * N for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                temp = 0
                for k in range(N):
                    temp += ((matrix1[i][k] % 1000) * (matrix2[k][j] % 1000)) % 1000
                temp %= 1000
                result[i][j] = temp
        return result
    
    def divide_and_conq(A, B):
        if B == 1:
            for i in range(len(A)):
                for j in range(len(A)):
                    A[i][j] %= 1000
            return A
        elif B % 2 == 0:
            divided_result_matrix = divide_and_conq(A, B // 2)
            return calc_matrix(divided_result_matrix, divided_result_matrix)
        else:
            divided_result_matrix = divide_and_conq(A, B // 2)
            return calc_matrix(A, calc_matrix(divided_result_matrix, divided_result_matrix))
    
    N, B = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    for row in divide_and_conq(A, B):
        print(*row)
    
    

soluiton()