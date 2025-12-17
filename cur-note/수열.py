def solution():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    sum_table = [0] * (N - K + 1) # 만약 10개의 숫자가 있고 3개씩 합을 구한다면... 1 2 3 4 5 6 7 8 9 10
    # 문제는 sum_table의 원소중 최대값
    sum_table[0] = sum(nums[:K])
    for i in range(1, len(sum_table)):
        sum_table[i] = sum_table[i - 1] + nums[i + K - 1] - nums[i - 1]
    
    print(max(sum_table))
    

solution()