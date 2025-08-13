def solution2():
    N = int(input())

    def hanoi(n, start, via, end):
        if n == 1:  # 원반의 갯수가 1개라면
            print(start, end)
        else:
            hanoi(n - 1, start, end, via)
            print(start, end)
            hanoi(n - 1, via, start, end)

    print(2 ** N - 1)
    if N <= 20:
        hanoi(N, 1, 2, 3)
    # A -> C로 n개의 원판을 옮기려면
    # 1. A -> B로 n-1개의 원판을 옮기고,
    # 2. A -> C로 가장 큰 원판을 옮기고,
    # 3. B -> C로 n-1개의 원판을 옮겨야한다.


solution2()