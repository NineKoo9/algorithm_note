def solution():
    def print_prime_num(n):
        import math
        
        if n == 0 or n == 1:
            print(2)
        else:
            # n 보다 큰 수들에 대해서 약수들을 찾아가야 한다. 그 중에서 
            # n에 대해서 약수를 찾는데... 
            find_prime = False
            while not find_prime :
                find_prime = True
                # n의 약수를 찾는다. 가 아니라 n이 소수인지 아닌지 판단하는 것이지
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        find_prime = False
                        n += 1
                        break
            print(n)
    
    T = int(input())
    test_cases = [int(input()) for _ in range(T)]
    for test_case in test_cases:
        print_prime_num(test_case)

def solution2():
    import math

    def get_prime(num):
        if num == 0 or num == 1:
            print(2)
        else:
            is_not_prime = True
            while is_not_prime:
                # 여기에 1 이 아닌 조건이 있어야하군...
                is_not_prime = False
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0: # 소수가 아님
                        is_not_prime = True
                        num += 1
                        break
            print(num)
                # 반복문을 돌았는데... 중지되지 않았다면? 소수란 녀석이군?

    T = int(input())
    tests = [int(input()) for _ in range(T)]
    for test in tests:
        # test 보다 크거나 같은 소수중 가장 작은 소수를 구해야한다.
        get_prime(test)
    pass

def solution3():
    def check_prime(n):
        # 이녀석이 소수인지 어떻게하지?
        # 약수들 중에서...
        # n이 소수가 아니라면... 루트n이하에서 약수를 가진다.
        if n == 0 or n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    T = int(input())
    for _ in range(T):
        n = int(input())
        # n보다 크거나 같은 소수를 구해야한다.
        while 1:
            if check_prime(n):
                print(n)
                break
            n += 1

solution3()