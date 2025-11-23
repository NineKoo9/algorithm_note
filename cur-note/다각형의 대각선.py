def solution():
    def factorial(n):
        if n == 1 or n == 0:
            return 1
        return n * factorial(n - 1)
    
    N = int(input())
    if N < 4:
        print(0)
    else:
        print(factorial(N) // (factorial(4) * factorial(N - 4)))

solution()