def solution():
    N = int(input())
    polls = [0] * 1111
    for _ in range(N):
        l, h = map(int, input().split())
        polls[l] = h

    prefix_max = [0] * 1111
    suffix_max = [0] * 1111
    for i in range(1, 1001):
        prefix_max[i] = max(prefix_max[i - 1], polls[i])
    for i in reversed(range(1, 1001)):
        suffix_max[i] = max(suffix_max[i + 1], polls[i])
    ans = 0
    for i in range(1, 1111):
        ans += min(prefix_max[i], suffix_max[i])
    print(ans)

solution()