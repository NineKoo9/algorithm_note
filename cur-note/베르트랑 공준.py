def solution():
    import math
    
    def check(num):
        if num == 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    
    test_cases = []
    while 1:
        num = int(input())
        if num == 0:
            break
        test_cases.append(num)
    
    for n in test_cases:
        # 여기서 n보다 크고 2n 보다 작은 소수의 갯수를 구해야한다.
        count = 0
        for i in range(n + 1, 2 * n + 1):
            # i 가 소수인지 아닌지 판단해야한다.
            if check(i):
                count += 1
        print(count)

solution()