def solution():
    def permutations(nums, M:int, path) -> list:
        if M == 0: # M의 카운트를 줄여나가는 방법으로 가보자.
            results.append(path)
            return
        
        for idx, num in enumerate(nums):
            tmp_path = path.copy()
            tmp_path.append(num)
            permutations(nums[idx+1:] if idx+1 < len(nums) else [], M-1, tmp_path)
            
    N, M = map(int, input().split())
    arrays = [i for i in range(1, N + 1)]
    results = []
    permutations(arrays, M, [])
    for result in results:
        print(*result)

solution()