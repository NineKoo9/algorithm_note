def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    prefix_sum = [0] * N
    prefix_sum[0] = arr[0]
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    ans = arr[0]
    min_prefix_sum = min(0, arr[0])
    for i in range(1, N):
        ans = max(ans, prefix_sum[i] - min_prefix_sum)
        min_prefix_sum = min(min_prefix_sum, prefix_sum[i])

    print(ans)

solution2()