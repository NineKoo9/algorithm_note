def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split())) + [0]

    s, e, count = 0, 1, 0  # 구간을 [s, e)로 정의
    total = A[s]
    while s <= e <= N:
        if total < M:
            total += A[e]
            e += 1
        elif total > M:
            total -= A[s]
            s += 1
        else:
            count += 1
            total -= A[s]
            total += A[e]
            s += 1
            e += 1

    print(count)

solution()