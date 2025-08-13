def solution():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    prefix_sum = [0] * (N + 1)

    prefix_sum[0] = nums[0]
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    max_value = -int(1e9)
    for i in range(N - K + 1):
        max_value = max(max_value, prefix_sum[i + K - 1] - (prefix_sum[i - 1] if i - 1 >= 0 else 0))
    print(max_value)

solution()