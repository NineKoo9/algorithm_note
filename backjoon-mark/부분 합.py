def solution():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    acc_sum = [arr[0]]
    for i in range(1, N):
        acc_sum.append(acc_sum[-1] + arr[i])
    start = 0
    end = 1
    INF = int(1e9)
    min_len = INF
    while 0 <= start < end < N:
        continuous_sub_sum = acc_sum[end] - (acc_sum[start - 1] if start - 1 >= 0 else 0)
        if continuous_sub_sum >= S:
            min_len = min(min_len, end - start + 1)
            start += 1
        else:
            end += 1
    #  혹시나 길이가 1인 녀석이 S보다 더 클 수 있다.
    for a in arr:
        if a >= S:
            min_len = 1
    # 만족하는 녀석이 없다
    print(min_len if min_len != INF else 0)

def solution2():
    from collections import deque

    N, S = map(int, input().split())  # N개짜리 수열리고 합이 S이상 되는 가장 짧은 수열을 찾는 것
    numbers = list(map(int, input().split()))
    min_length = int(1e6) + 1
    pointer = -1
    current_sum = 0
    index_queue_of_sum = deque()
    while pointer < N:
        if current_sum >= S:
            min_length = min(min_length, len(index_queue_of_sum))
            first_index = index_queue_of_sum.popleft()
            current_sum -= numbers[first_index]
            continue
        pointer += 1
        if pointer >= N:
            break
        current_sum += numbers[pointer]
        index_queue_of_sum.append(pointer)

    print(min_length if min_length != int(1e6) + 1 else 0)

def solution3():
    N, S = map(int, input().split())  # N개의 수열에서 합이 S 이상이 되는 가장 짧은 부분 수열 찾기
    numbers = list(map(int, input().split()))

    min_length = float('inf')
    left = 0
    current_sum = 0

    # 슬라이딩 윈도우를 위한 right 포인터 이동
    for right in range(N):
        current_sum += numbers[right]

        # 합이 S 이상인 부분 수열을 찾으면, left 포인터를 이동하여 최소 길이를 찾음
        while current_sum >= S:
            min_length = min(min_length, right - left + 1)
            current_sum -= numbers[left]
            left += 1

    # min_length가 업데이트되지 않은 경우, 부분 수열의 합이 S 이상인 경우가 없음
    print(min_length if min_length != float('inf') else 0)

def solution4():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    # 누적합을 구한다.
    prefix_sum_A = [0] * len(A)
    prefix_sum_A[0] = A[0]
    for i in range(1, len(A)):
        prefix_sum_A[i] = prefix_sum_A[i - 1] + A[i]

    # 투 포인터를 이용해 연속적인 수들을 관찰한다.
    # 이런 것은 슬라이딩 윈도우라고 표현해야하나?
    s, e = 0, 0
    INF = int(1e9)
    min_length = INF
    while 0 <= s <= e < N:
        continuous_sum = prefix_sum_A[e] - (prefix_sum_A[s - 1] if s - 1 >= 0 else 0)
        if continuous_sum >= S:
            min_length = min(min_length, e - s + 1)
            s += 1
        elif continuous_sum < S:
            e += 1
    print(min_length if min_length != INF else 0)

solution4()