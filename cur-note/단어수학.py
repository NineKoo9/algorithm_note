from collections import defaultdict

def solution():
    N = int(input())
    words = [input() for _ in range(N)]

    alpha = defaultdict(int)
    for word in words:
        for i in range(1, len(word) + 1):
            ch = word[-i]
            alpha[ch] += pow(10, i - 1)

    values = []
    for k, v in alpha.items():
        values.append((v, k))

    values.sort(reverse=True)

    result = 0
    num = 9
    for value in values:
        v, k = value
        result += v * num
        num -= 1
    print(result)

solution()