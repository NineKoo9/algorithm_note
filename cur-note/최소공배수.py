def solution():
    def get_min_mul(a, b):
        max_yak = 1
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                max_yak = max(max_yak, i)
        return a * b // max_yak
        
    
    T = int(input())
    nums = [list(map(int, input().split())) for _ in range(T)]
    for a, b in nums:
        print(get_min_mul(a, b))
        
def solution2():
    import math
    
    a, b = map(int, input().split())
    max_yak = math.gcd(a, b)
    print(a * b // max_yak)
    
solution2()