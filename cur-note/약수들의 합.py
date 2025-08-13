def solution():
    def is_perfect_num(n):
        divs: list = []
        for i in range(1, n):
            if n % i == 0:
                divs.append(i)
        if sum(divs) == n:
            s = " + ".join([str(div) for div in divs])
            print(f"{n} = {s}")
        else:
            print(f"{n} is NOT perfect.")
    while 1:
        n = int(input())
        if n == -1:
            break
        is_perfect_num(n)


solution()
