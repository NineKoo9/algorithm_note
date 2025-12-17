def solution():
    n = int(input())
    m = 2 * n - 1
    # 2n-1까지 별찍어 나가야 한다.
    for i in range(m):
        for j in range(m):
            if (j <= -(i - (m - 1)) + n - 1)\
                    and (j >= - i + n - 1) \
                    and (j - (m-1) <= i -(n-1))\
                    and (j >= i -(n-1)):
                print("*", end="")
            else:
                print(" ", end="")
        print("") if i < m-1 else print("", end="")

solution()
