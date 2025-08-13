def solution():
    def get_sum_result(i, j):
        return sum_table[j] - sum_table[i - 1] if i - 1 >= 0 else sum_table[j]
    
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    start_end_lst = [tuple(map(int, input().split())) for _ in range(M)]
    sum_table = [0] * N
    sum_table[0] = nums[0]
    for n in range(1, N):
        sum_table[n] += sum_table[n - 1] + nums[n]
    for start, end in start_end_lst:
        print(get_sum_result(start - 1, end - 1))

solution()