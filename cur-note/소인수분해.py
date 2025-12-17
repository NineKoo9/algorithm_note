def solution():
    def is_prime(n):
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                return False
        return True

    # N은 천만까지 주어진다.
    # 말도 안되는 것이구나... 최악의 경우 천만 * 루트천만정도라니...
    N = int(input())
    prime_num = [num for num in range(2, N + 1) if is_prime(num)]
    for num in prime_num:
        if N == 1:
            break
        while N % num == 0:
            N = N // num
            print(num)

def solution2():
    N = int(input())
    prime_num = 2
    while N != 1:
        if N % prime_num == 0:
            print(prime_num)
            N //= prime_num
        else:
            prime_num += 1


solution()

# 소인수분해라는 것은 소수로 계속 나눠가는 것이니까... 소수를 구해봐야 겠군.
# 시간초과가 발생하였다.
