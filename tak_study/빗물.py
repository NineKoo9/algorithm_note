def solution():
    H, W = map(int, input().split())
    arr = list(map(int, input().split()))

    prefix_max = [0] * W
    suffix_max = [0] * W

    prefix_max[0] = arr[0]
    suffix_max[-1] = arr[-1]
    for i in range(1, W):
        prefix_max[i] = max(prefix_max[i - 1], arr[i])
    for ri in reversed(range(W - 1)):
        suffix_max[ri] = max(suffix_max[ri + 1], arr[ri])

    top_arr = [0] * W
    for i in range(W):
        top_arr[i] = min(prefix_max[i], suffix_max[i])

    ans = 0
    for i in range(W):
        ans += top_arr[i] - arr[i]
    print(ans)


solution()