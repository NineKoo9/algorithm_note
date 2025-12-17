def solution():
    A_size, B_size = map(int, input().split())
    A_set = {*map(int, input().split())}
    B_set = {*map(int, input().split())}
    a_b = A_set - B_set
    b_a = B_set - A_set
    print(len(a_b | b_a))

solution()