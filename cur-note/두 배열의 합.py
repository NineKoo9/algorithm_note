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

def solution3():
    def my_bisect_left(arr, target):
        s = 0
        e = len(arr) - 1
        ans = len(arr)
        while s <= e:
            m = (s + e) // 2
            if arr[m] < target:
                s = m + 1
            else:  # arr[m] >= target
                e = m - 1
                ans = m
        return ans

    def my_bisect_right(arr, target):
        s = 0
        e = len(arr) - 1
        ans = len(arr)
        while s <= e:
            m = (s + e) // 2
            if arr[m] <= target:
                s = m + 1
            else: # arr[m] > target
                e = m - 1
                ans = m
        return ans

    T = int(input())

    n = int(input())
    A = list(map(int, input().split()))

    m = int(input())
    B = list(map(int, input().split()))

    # 부배열의 합을 각각 더해서 T가 되는 쌍을 구해야한다.
    # 먼저 A의 모든 부배열의 합을 구한다. 중복된 것도 있을 수 있으며 서로 다른 것으로 처리한다.
    # 합을 빠르게 구하기 위해서 prefixSum을 구한다.
    
    # prefix_sum[i] 는 [0, i)구간의 모든 합이다.
    prefix_sum_A = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum_A[i] = prefix_sum_A[i - 1] + A[i - 1]

    prefix_sum_B = [0] * (m + 1)
    for i in range(1, m + 1):
        prefix_sum_B[i] = prefix_sum_B[i - 1] + B[i - 1]

    sub_A_values = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_A_values.append(prefix_sum_A[j] - prefix_sum_A[i])

    sub_B_values = []
    for i in range(m):
        for j in range(i + 1, m + 1):
            sub_B_values.append(prefix_sum_B[j] - prefix_sum_B[i])

    ans = 0
    sub_B_values.sort()
    for sub_A_value in sub_A_values:
        # 이제 B의 서브 합에서 targetvalue가 몇개 있는지 구하면 된다.
        target_value = T - sub_A_value
        sub_B_count = my_bisect_right(sub_B_values, target_value) - my_bisect_left(sub_B_values, target_value)
        ans += sub_B_count
    print(ans)
    
solution3()