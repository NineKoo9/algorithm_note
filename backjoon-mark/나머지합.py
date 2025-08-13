def solution():
    from collections import defaultdict
    
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    sum_table = [0] * N
    remain_count = defaultdict(int)
    for i in range(N):
        sum_table[i] = (sum_table[i - 1] if i - 1 >= 0 else 0) + array[i]
        remain_count[sum_table[i] % M] += 1
    count = remain_count[0] # 여기서는 처음부터 j 번까지인 경우를 카운트
    for r, c in remain_count.items():
        count += ((c * (c - 1)) // 2) # 여기서는 i부터 j번까지 카운트
    print(count)

solution()