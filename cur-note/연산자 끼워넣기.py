def solution():
    def operate(operations, result, n):
        if sum(operations) == 0:  # 더이상 남은 연산이 없다면?
            max_min_results[0] = max(max_min_results[0], result)
            max_min_results[1] = min(max_min_results[1], result)
            return

        for operation, count in enumerate(operations):
            if operation == 0 and count > 0:  # 덧셈
                tmp_result = result + num_arrays[n + 1]
                tmp_operations = operations.copy()
                tmp_operations[0] -= 1
                operate(tmp_operations, tmp_result, n + 1)
            elif operation == 1 and count > 0:  # 뺄셈
                tmp_result = result - num_arrays[n + 1]
                tmp_operations = operations.copy()
                tmp_operations[1] -= 1
                operate(tmp_operations, tmp_result, n + 1)
            elif operation == 2 and count > 0:  # 곱셈
                tmp_result = result * num_arrays[n + 1]
                tmp_operations = operations.copy()
                tmp_operations[2] -= 1
                operate(tmp_operations, tmp_result, n + 1)
            elif operation == 3 and count > 0:  # 나눗셈
                tmp_result = (result // num_arrays[n + 1]) if result > 0 else -1 * ((-1 * result) // num_arrays[n + 1])
                tmp_operations = operations.copy()
                tmp_operations[3] -= 1
                operate(tmp_operations, tmp_result, n + 1)

    N = int(input())
    num_arrays = list(map(int, input().split()))
    operate_arrays = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈 순이다
    INF = int(1e9)
    max_min_results = [-INF, INF]  # 최대, 최소
    operate(operate_arrays, num_arrays[0], 0)  # 0번째 부터... 첫번째 수를 우선 집어넣었다.
    print(*max_min_results, sep="\n")


solution()
