def solution():
    def operate(a, b, c):
        if b == 1:
            return a % c
        elif b % 2 == 0:
            return (operate(a, b//2, c) ** 2) % c
        else: # b가 홀수인경우
            return ((operate(a, b//2, c ) ** 2) * a % c) % c
    
    
    A, B, C = map(int, input().split())
    
    print(operate(A, B, C))


solution()