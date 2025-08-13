def solution():
    mod = 10**9 + 7

    N = int(input().strip())
    S = input().strip()
    preW  = [0] * (N+1)
    preWH = [0] * (N+1)
    Epos  = []

    for i, c in enumerate(S, start=1):
        preW[i]  = preW[i-1]
        preWH[i] = preWH[i-1]
        if c == 'W':
            preW[i] += 1
        elif c == 'H':
            preWH[i] = (preWH[i] + preW[i-1]) % mod
        elif c == 'E':
            Epos.append(i)

    M = len(Epos)
    if M < 2:
        print(0)
        return

    pow2 = [1] * (M+1)
    for i in range(1, M+1):
        pow2[i] = (pow2[i-1] * 2) % mod

    ans = 0
    for k in range(M-1):
        pos    = Epos[k]
        remain = M - (k+1)
        waysE  = (pow2[remain] - 1) % mod
        ans    = (ans + preWH[pos] * waysE) % mod

    print(ans)


# 하... 이거 시간초과 미치도록 걸리네 어떻게 하지?
def solution2():
    N = int(input())
    S = list(input())
    prefix_count_W = [0] * N
    prefix_count_WH = [0] * N
    prefix_count_WHE = [0] * N
    posE = []
    mod = int(1e9) + 7

    for i in range(N):
        ch = S[i]
        prefix_count_W[i] = prefix_count_W[i - 1] if i - 1 >= 0 else 0
        prefix_count_WH[i] = prefix_count_WH[i - 1] if i - 1 >= 0 else 0
        prefix_count_WHE[i] = prefix_count_WHE[i - 1] if i - 1 >= 0 else 0
        if ch == "W":
            prefix_count_W[i] += 1
        elif ch == "H":
            prefix_count_WH[i] += prefix_count_W[i] % mod
        elif ch == "E":
            prefix_count_WHE[i] += prefix_count_WH[i] % mod
            posE.append(i)

    ans = 0
    len_posE = len(posE)
    for idx, e_pos in enumerate(posE):
        ans += ((prefix_count_WHE[e_pos - 1] * (2 ** (len_posE - idx - 1))) % mod)
    print(ans)

solution2()