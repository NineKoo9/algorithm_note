from bisect import bisect_left, bisect_right

def solution():
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    sum_A, sum_B = [], []
    for i in range(n):
        s = A[i]
        sum_A.append(s)
        for j in range(i + 1, n):
            s += A[j]
            sum_A.append(s)

    for i in range(m):
        s = B[i]
        sum_B.append(s)
        for j in range(i + 1, m):
            s += B[j]
            sum_B.append(s)

    count = 0
    sum_B.sort()
    for i in range(len(sum_A)):
        value = T - sum_A[i]

        hi = bisect_right(sum_B, value)
        lo = bisect_left(sum_B, value)
        count += (hi - lo)

    print(count)

def solution2():
    from bisect import bisect_left, bisect_right

    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    # 누적합 값을 초기화한다.
    prefix_sum_A = [A[0]]
    for i in range(1, n):
        prefix_sum_A.append(prefix_sum_A[-1] + A[i])

    prefix_sum_B = [B[0]]
    for i in range(1, m):
        prefix_sum_B.append(prefix_sum_B[-1] + B[i])

    # 지금부터 배열 B의 모든 값들을 구한다.
    B_sums = B.copy()
    for i in range(m - 1):
        for j in range(i + 1, m):
            # i != j B[i][j] 의 합이다.
            value = prefix_sum_B[j] - (prefix_sum_B[i - 1] if i - 1 >= 0 else 0)
            B_sums.append(value)
    B_sums.sort()

    count = 0
    for i in range(n):
        for j in range(i, n):
            # A[i][j]인 값이고 서로 같을 수 있다.
            A_i_j = prefix_sum_A[j] - (prefix_sum_A[i - 1] if i - 1 >= 0 else 0)
            target_value = T - A_i_j
            s = bisect_left(B_sums, target_value)
            e = bisect_right(B_sums, target_value)
            count += (e - s)
    print(count)

solution2()