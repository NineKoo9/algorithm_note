def solution():
    # 10 + 20 - 30 + 50 + 20 - 30 여기서 괄호를 쳐서 최소로 만들려면 어떻게 하지?
    # 괄호를 친다는 말은.. 연산을 먼저 수행한다는 것인데.. 최대한 - 연산의 결과가 커지도록 하는 것이 중요하겠다.
    # 이제 중요한 것은 어떻게 파싱해 나갈까가 문제다.
    # 사실상 생각해보니까... 마이너스가 하나라도 있으면 그냥 전부다... 마이너스로 넣어버리면 되네....
    S = input()
    pointer = 0
    num_lst = []
    operation_lst = []
    while pointer < len(S):
        start_point = pointer
        while pointer < len(S) and S[pointer].isnumeric():
            pointer += 1
        end_pointer = pointer
        num_lst.append(int(S[start_point:end_pointer]))
        if end_pointer < len(S):
            operation_lst.append(S[end_pointer])
        pointer += 1
    result = [num_lst[0]]
    minus_flag = False
    for idx, operation in enumerate(operation_lst, start = 1):
        if operation == '-':
            minus_flag = True
        if not minus_flag:
            result.append(num_lst[idx])
        else:
            result.append(-1 * num_lst[idx])
    print(sum(result))

def solution2():
    S = input()
    operands = []
    operators = []
    cur = ""
    for ch in S:
        if ch.isnumeric():
            cur += ch
        else:
            operands.append(int(cur))
            operators.append(ch)
            cur = ""
    operands.append(int(cur))
    dp_min = [int(1e9)] * len(operands)
    dp_min[0] = operands[0] # 최소
    minus_flag = False
    for i in range(1, len(operands)):
        if operators[i - 1] == "+":
            dp_min[i] = min(dp_min[i], dp_min[i - 1] + operands[i], (dp_min[i - 1] - operands[i]) if minus_flag else int(1e9))
        else: # operators == "-"
            minus_flag = True
            dp_min[i] = min(dp_min[i], dp_min[i - 1] - operands[i])
    print(dp_min[-1])

def solution3():
    i = input()
    operands = []
    operators = []
    num = ""
    for ch in i:
        if not ch.isnumeric():
            operators.append(ch)
            operands.append(int(num))
            num = ""
            continue
        num += ch
    operands.append(int(num))

    # 숫자와 연산자 분리
    N = len(operands)

    INF = int(1e9)
    max_dp = [[-INF] * N for _ in range(N)]
    min_dp = [[INF] * N for _ in range(N)]

    # 먼저 step이 0인 경우를 초기화하자.
    for i in range(N):
        max_dp[i][i] = operands[i]
        min_dp[i][i] = operands[i]

    # 이제 step이 1인 경우부터 탐색을 하자.
    for step in range(1, N):
        for i in range(N - step):
            j = i + step
            for k in range(i, j):
                if operators[k] == "+":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                else:  # operands[k] == "-"
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])
    print(min_dp[0][N - 1])


        
solution3()