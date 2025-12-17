from itertools import permutations


# 분할정복을 구현하는 것 자체가 쉽지가 않네...
# 최종적인 분할정복 위치가 무엇이지? 연산자를 순서대로 다 처리한 경우다.
# split("*")이 빈칸? 을 던질 수 있는 것에 유의하자.
def calc(operator, operands):
    result = int(operands[0])
    for operand in operands[1:]:
        if operand == "":
            continue
        if operator == "*":
            result *= int(operand)
        elif operator == "-":
            result -= int(operand)
        elif operator == "+":
            result += int(operand)
    # print(f"operator: {operator}, operands: {operands}, result: {result}")
    return result


def div_and_conq(priority_order, expression, n):
    operator = priority_order[n]
    if n == 2:
        return calc(operator, expression.split(operator))
    else:
        return calc(operator, [div_and_conq(priority_order, sub_expression, n + 1) for sub_expression in
                               expression.split(operator)])


def solution(expression):
    max_value = 0
    for priority_order in permutations(["*", "+", "-"], 3):  # 6!
        max_value = max(max_value, abs(int(div_and_conq(priority_order, expression, 0))))
    return max_value


