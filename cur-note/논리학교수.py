def solution():
    from collections import defaultdict
     
    N = int(input())
    nums = list(map(int, input().split()))
    counter = defaultdict(int)
    
    for num in nums:
        counter[num] += 1
        
    answer = -1 # 정답이 없는 경우
    for t in range(N + 1):
        if counter[t] == t:
            answer = max(answer, t)
    print(answer)

solution()