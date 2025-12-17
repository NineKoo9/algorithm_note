def solution():
    import math
    
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    b_max_yak = math.gcd(b1, b2)
    a1, b1, a2, b2 = (a1 * b2) // b_max_yak, (b1 * b2) // b_max_yak, (a2 * b1) // b_max_yak, (b1 * b2) // b_max_yak
    a = a1 + a2
    b = b1
    while math.gcd(a, b) != 1:
        common_yak = math.gcd(a, b)
        a = a // common_yak
        b = b // common_yak
    print(a, b)

solution() 