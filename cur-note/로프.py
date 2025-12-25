def solution():
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    nums.sort()
    
    max_weight = 0
    for idx, num in enumerate(nums):
        # idx 번째 줄까지 포함했을때 들 수 있는 최대의 무게는?
        w = num * (N - idx)
        max_weight = max(max_weight, w)
    print(max_weight)

solution()