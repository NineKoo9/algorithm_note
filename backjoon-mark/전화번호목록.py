def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = [input() for _ in range(n)]
        numbers.sort()

        # 정렬했고... 이제 앞의 녀석과
        result = "YES"
        for idx, number in enumerate(numbers[:-1]):
            if numbers[idx+1].startswith(number):
                result = "NO"
                break
        print(result)



solution()