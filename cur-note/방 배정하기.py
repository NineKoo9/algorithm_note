def solution():
    A, B, C, N = map(int, input().split())
    for x in range(1 + (N // A) ):
        for y in range(1 + (N // B)):
            for z in range(1 + (N // C)):
                if A * x + B * y + C * z == N:
                    print(1)
                    exit()
    print(0)

solution()