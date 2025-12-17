def solution(expression):
    from itertools import permutations
    def calculate(num_lst, oper_lst, priority):
        for op in priority:
            while op in oper_lst:
                # 이 안에 있는 연산자는 모두 계산해야지?
                idx = oper_lst.index(op)
                oper_lst.pop(idx)
                if op == "*":
                    result = num_lst[idx] * num_lst[idx + 1]
                    num_lst[idx] = result
                    num_lst.pop(idx + 1)
                elif op == "+":
                    result = num_lst[idx] + num_lst[idx + 1]
                    num_lst[idx] = result
                    num_lst.pop(idx + 1)
                else:  # 여기서는 "-" 이겠다.
                    result = num_lst[idx] - num_lst[idx + 1]
                    num_lst[idx] = result
                    num_lst.pop(idx + 1)
        return abs(sum(num_lst))

    operands = []
    operations = []
    priorites = permutations(("*", "-", "+"), 3)
    operand = ""
    for c in expression:
        if not c.isdigit():
            operands.append(int(operand))
            operations.append(c)
            operand = ""
            continue
        operand += c
    operands.append(int(operand))
    max_value = 0
    for priority in priorites:
        max_value = max(max_value, calculate(operands.copy(), operations.copy(), priority))

    answer = max_value
    return answer



# 2번째 풀이..

def calc_operator(operator, num1, num2):
    if operator == "*":
        return num1 * num2
    elif operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2


def calc(priority, operands, operators):
    for target_operator in priority:  # 해봤자 최대 3개
        while target_operator in operators:
            idx = operators.index(target_operator)
            result = calc_operator(target_operator, operands[idx], operands[idx + 1])
            operands[idx] = result
            operands.pop(idx + 1)
            operators.pop(idx)
    return abs(operands[0])


def solution(expression):
    from itertools import permutations

    operands = []
    operators = []
    temp = ""
    for ch in expression:
        if not ch.isnumeric():
            operands.append(int(temp))
            operators.append(ch)
            temp = ""
        else:
            temp += ch
    operands.append(int(temp))
    max_value = 0
    for priority in permutations(["*", "+", "-"], 3):
        max_value = max(max_value, calc(priority, operands.copy(), operators.copy()))
    return max_value


# 3번째 풀이... 이런 방법도 있다...! eval이란거 신기하네 그렇지만.. 앞선 풀이보단 속도가 느리다.
from itertools import permutations

def div_conqer(priority, expression, n):
    if n == 2:
        return str(eval(expression))
    if priority[n] == "*":
        return str(eval("*".join([div_conqer(priority, part, n + 1) for part in expression.split("*")])))
    elif priority[n] == "+":
        return str(eval("+".join([div_conqer(priority, part, n + 1) for part in expression.split("+")])))
    elif priority[n] == "-":
        return str(eval("-".join([div_conqer(priority, part, n + 1) for part in expression.split("-")])))

def solution(expression):
    max_value = 0
    for priority in permutations(["*", "+", "-"], 3):
        max_value = max(max_value, abs(int(div_conqer(priority, expression, 0))))
    return max_value