def solution():
    A, B = map(int, input().split())
    answer = []
    for x in range(-2000, 2001):
        if (x ** 2 + 2 * A * x + B) == 0:
            answer.append(x)
    print(*answer)

solution()

