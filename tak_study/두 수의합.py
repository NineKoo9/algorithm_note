def solution():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    A.sort()
    s = 0
    e = N - 1
    count = 0
    while s < e:
        if A[s] + A[e] == X:
            count += 1
            s += 1
            e -= 1
        elif A[s] + A[e] > X:
            e -= 1
        elif A[s] + A[e] < X:
            s += 1
    print(count)

solution()