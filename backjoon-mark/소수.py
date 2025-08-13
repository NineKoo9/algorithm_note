def solution():
    def is_prime(n):
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                return False
        return True
    M = int(input())
    N = int(input())
    prime_num= []
    for num in range(M, N + 1):
        if num == 1:
            continue
        if is_prime(num):
            prime_num.append(num)
    if prime_num:
        print(sum(prime_num))
        print(min(prime_num))
    else:
        print(-1)


solution()