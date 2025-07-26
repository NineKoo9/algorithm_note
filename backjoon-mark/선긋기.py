def solution():
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    lines.sort()

    ans = 0
    s = lines[0][0]
    e = lines[0][1]
    for n_s, n_e in lines:
        if e <= n_s:
            ans += e - s
            s = n_s
            e = n_e
        elif n_s < e < n_e:
            e = n_e
    ans += e - s
    print(ans)

solution()