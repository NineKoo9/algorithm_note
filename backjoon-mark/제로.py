def solution():
    K = int(input())
    integers = [int(input()) for _ in range(K)]
    stack = []
    for i in integers:
        if i == 0:
            stack.pop()
            continue
        stack.append(i)
    print(sum(stack))

solution()