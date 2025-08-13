def solution():
    # 당장에 드는 생각은...
    N = int(input())
    INF = int(1e9)
    min_value = INF
    for n in range(N+1):
        diff = N - n
        if diff == sum(map(int, str(n))):
            min_value = min(min_value, n)
    print(min_value if min_value != INF else 0)


solution()