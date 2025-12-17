def solution():
    def calc_matrix(matrix1, matrix2):
        l = len(matrix1)
        result = [[0] * l for _ in range(l)]
        for i in range(l):
            for j in range(l):
                temp = 0
                for k in range(l):
                    temp += ((matrix1[i][k] % divider) * (matrix2[k][j] % divider)) % divider
                result[i][j] = temp % divider
        return result
    
    def calc_zero_one(matrix):
        matrix2 = [1, 0]
        result = [0, 0]
        for i in range(2):
            for k in range(2):
                result[i] += matrix[i][k] * matrix2[k]
        return result
    
    def divide_and_conq(matrix, n):
        if n == 1:
            for i in range(2):
                for j in range(2):
                    matrix[i][j] %= divider
            return matrix
        elif n % 2 == 0:
            divided_result = divide_and_conq(matrix, n // 2)
            return calc_matrix(divided_result, divided_result)
        else:
            divided_result = divide_and_conq(matrix, n // 2)
            return calc_matrix(calc_matrix(divided_result, divided_result), [[1, 1], [1, 0]])
    
    n = int(input())
    divider = int(1e9) + 7
    # n번째 피보나치수를 구해야한다.
    result_matrix = divide_and_conq([[1, 1], [1, 0]], n)
    print(calc_zero_one(result_matrix)[1])

solution()