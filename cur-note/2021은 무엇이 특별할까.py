import math
import bisect

def solution():
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        if n == 2:
            return True
        
        for k in range(2, int(math.sqrt(n)) + 1):
            if n % k == 0:
                return False
        return True
    
    
    N = int(input())
    
    # 소수들을 먼저 초기화한다. 소수는 100이하면 충분하다. 그렇게 만지가 않다.
    prime_numbers = [i for i in range(111) if is_prime(i)]
    
    # 이제 특별한 수들을 모두 구한다.
    special_numbers = [prime_numbers[i] * prime_numbers[i + 1] for i in range(len(prime_numbers) - 1)]
    
    ans_idx = bisect.bisect_right(special_numbers, N)
    print(special_numbers[ans_idx])

solution()