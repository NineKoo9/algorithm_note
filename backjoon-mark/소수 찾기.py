def solution():
    def find_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    N = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for num in nums:
        if num != 1 and find_prime(num):
            count += 1
    print(count)


solution()
