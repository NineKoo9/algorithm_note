def solution():
    def fail_func(S):
        n = len(S)
        F = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and S[i] != S[j]:
                j = F[j - 1]
            if S[i] == S[j]:
                j += 1
                F[i] = j
        return F

    S = input()
    P = input()

    # 먼저 p에 대한 실패함수를 만들자.
    P_fail_func = fail_func(P)
    j = 0
    for i in range(len(S)):
        while j > 0 and S[i] != P[j]:
            j = P_fail_func[j - 1]
        if S[i] == P[j]:
            j += 1
        if j == len(P): # 일치함을 찾음
            print(1)
            return
    print(0)
solution()