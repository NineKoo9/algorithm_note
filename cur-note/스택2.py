def solution():
    N = int(input())
    orders = [tuple(map(int, input().split())) for _ in range(N)]
    stack = []
    for order in orders:
        if len(order) > 1:
            _, n = order
            stack.append(n)
        elif order[0] == 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif order[0] == 3:
            print(len(stack))
        elif order[0] == 4:
            if stack:
                print(0)
            else:
                print(1)
        else:
            if stack:
                print(stack[-1])
            else:
                print(-1)


solution()