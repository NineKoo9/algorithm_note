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

def solution2():    
    def operate(a, b, c):
        if b == 1:
            return a % C
        elif b % 2 == 0:
            return (pow(operate(a, b // 2, c), 2)) % c
        else:
            return (pow(operate(a, b // 2, c), 2) * (a % c)) % c
    
    A, B, C = map(int, input().split())
    # A를 B번 곱한 수를 알고 싶다.
    # ans % C = (A * B) % C = (A % C * B % C) % C
    # 아 거듭제곱 문제구나?
    # (A * A * A * A) % C = K % C = ((A % C) * (A % C) * (A % C) * (A % C)) % C
    # 문제는 이것을 B의 최대 값인 21억번까지 할 수 없는 것이다. 어떻게 최적화를 할 수 있을까?
    # 제일 작은 것에서 2배씩 늘려가면 충분히 겹치는 연산이 있다는 것을 알 수 있다.
    print(operate(A, B, C))

solution2()