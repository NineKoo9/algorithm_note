def solution():
    def return_coin(num):
        coins = [25, 10, 5, 1]
        result = []
        for coin in coins:
            count = num // coin
            num = num % coin
            result.append(count)
        print(" ". join([str(c) for c in result]))
    T = int(input())
    test_case = [int(input()) for _ in range(T)]
    for cent in test_case:
        return_coin(cent)


solution()