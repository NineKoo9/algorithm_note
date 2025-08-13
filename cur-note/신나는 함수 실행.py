def solution():
    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            dp[(a, b, c)] = 1
            return 1

        if a > 20 or b > 20 or c > 20:
            dp[(a, b, c)] = dp[(20, 20, 20)] if (20, 20, 20) in dp else w(20, 20, 20)
            return dp[(a, b, c)]

        if a < b < c:
            dp[(a, b, c)] = (dp[(a, b, c - 1)] if (a, b, c - 1) in dp else w(a, b, c - 1)) \
                            + (dp[(a, b - 1, c - 1)] if (a, b - 1, c - 1) in dp else w(a, b - 1, c - 1)) \
                            - (dp[(a, b - 1, c)] if (a, b - 1, c) in dp else w(a, b - 1, c))
            return dp[(a, b, c)]
        else:
            dp[(a, b, c)] = (dp[(a-1, b, c)] if (a-1, b, c) in dp else w(a - 1, b, c)) \
                            + (dp[(a-1, b-1, c)] if (a-1, b-1, c) in dp else w(a - 1, b - 1, c)) \
                            + (dp[(a-1, b, c-1)] if (a-1, b, c-1) in dp else w(a - 1, b, c - 1)) \
                            - (dp[(a-1, b-1, c-1)] if (a-1, b-1, c-1) in dp else w(a - 1, b - 1, c - 1))
            return dp[(a, b, c)]

    dp = {}
    while 1:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')

solution()