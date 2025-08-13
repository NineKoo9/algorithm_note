def solution():
    import math
    
    def check(n) -> bool:
        # 소수인지 판단한다.
        if n == 0 or n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    M, N = map(int, input().split())
    for num in range(M, N+1):
        #num이 소수면 출력한다.
        if check(num):
            print(num)
    
    pass

solution()