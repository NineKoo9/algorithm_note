import math
import sys

def solution():
    def check_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    # 소수들을 제너레이터를 이용할까?
    def find_gold_bach_part_num(n) -> int:
        # n이 최대 100만인데... 여기서 50만이 소요될수있다.
        # n = a + b 이고 a와 b가 소수라면 그것을 더한 것은? a = n - b 도 소수란 말이다. 
        count = 0
        for a in prime_nums:
            b = n - a
            if a > b:
                break
            if check_prime(b):
                count += 1
        return count
    
    T = int(sys.stdin.readline())
    test_cases = [int(sys.stdin.readline()) for _ in range(T)]
    prime_nums = [i for i in range(2, int(1e6)) if check_prime(i)]
    
    for num in test_cases:
        # num이 골드바흐파티션의 갯수를 구한다
        print(find_gold_bach_part_num(num))


def solution2():
    T = int(sys.stdin.readline())
    test_cases = [int(sys.stdin.readline()) for _ in range(T)]
    # 소수 초기화
    MAX = int(1e6) + 1
    prime_nums = []
    prime_check = [1] * MAX
    prime_check[0] = 0
    prime_check[1] = 0
    for n in range(2, MAX):
        if prime_check[n] == 0:
            continue
        prime_nums.append(n)
        for i in range(2, (MAX // n) + 1):
            if n * i < MAX:
                prime_check[n * i] = 0
                
    for test_num in test_cases:
        # 이제 이 테케들이 소수의 합으로 나눠지는지 확인해야겠구만...
        count = 0
        for prime_num1 in prime_nums:
            prime_num2 = test_num - prime_num1
            if prime_num1 > prime_num2:
                break
            if prime_check[prime_num2]:
                count += 1
        print(count)

def solution3():
    import math
    def is_not_prime(num):
        if num == 0 or num == 1:
            return True
        # num이 소수인지 아닌지 판단한다.
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return True
        return False
    def init_prime_nums():
        max_nums = int(1e6) + 1
        nums = [1 for _ in range(max_nums)]
        # 자 인덱스에 해당하는 수가 소수인지 아닌지 체크하는 것이다.
        nums[0] = 0
        nums[1] = 0
        for i in range(2, max_nums):
            # 0이라면 이미 소수가 아니니까 체크를 안한다.
            if nums[i] == 0:
                continue
            # if is_not_prime(i):
            #     # i 가 프라임이 아니라면... 그 배수도 모두 소수가 아니다.
            #     nums[i] = 0
            for j in range(2, max_nums):
                if i * j >= max_nums:
                    break
                nums[i * j] = 0
        # 자 이제... 1로 남은 녀석들만 소수이다.
        prime_nums = [i for i in range(max_nums) if nums[i] == 1]
        return prime_nums

    T = int(input())
    test_nums = [int(input()) for _ in range(T)]
    prime_nums = init_prime_nums()
    for test_num in test_nums:
        # 소수중에서 test_num 을 만족하는 쌍이 몇개인지 찾자
        start = 0
        end = len(prime_nums) - 1
        count = 0
        while 0 <= start <= end < len(prime_nums):
            if prime_nums[start] + prime_nums[end] > test_num:
                end -= 1
            elif prime_nums[start] + prime_nums[end] < test_num:
                start += 1
            else: # 여기서 찾았다!
                count += 1
                start += 1
                end -= 1
        print(count)

def solution4():
    def check_prime(n):
        if n == 0 or n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % 2 == 0:
                return False
        return True

    is_prime = [1] * 1000001  # 먼저 기본적으로 모두 소수라고 가정하고 탐색하자.
    for n in range(1000001):
        if not is_prime[n]:
            continue
        if check_prime(n):
            i = 2
            while n * i < 1000001:
                is_prime[n * i] = 0
                i += 1
        else:
            is_prime[n] = 0
    prime_nums = []
    for i in range(1000001):
        if is_prime[i]:
            prime_nums.append(i)
    prime_nums.sort()

    T = int(input())
    for _ in range(T):
        N = int(input())
        # 이제 N을 두개의 소수의 합으로 구해야하는데....
        # 투 포인터를 이용할까?
        s = 0
        e = len(prime_nums) - 1
        count = 0
        while s <= e:
            if prime_nums[s] + prime_nums[e] == N:
                count += 1
                s += 1
                e -= 1
            elif prime_nums[s] + prime_nums[e] < N:
                s += 1
            elif prime_nums[s] + prime_nums[e] > N:
                e -= 1
        print(count)
    pass


solution4()

# 역시 그냥 이러한 풀이는 시간초과를 발생시키네...
# 100만 까지 모든수에 대해서 프라임이냐 아니냐를 판단하는것은 너무 오래 걸린다.
# 그렇다면 모든 수를 구해놓고 프라임인지 아닌지 체크해 놓는것이 어떤가로 가는게 좋아보인다...?