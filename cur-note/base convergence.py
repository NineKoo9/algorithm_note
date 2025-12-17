def solution():
    A, B = map(int, input().split())
    m = int(input())
    nums = list(map(int, input().split()))
    
    # A진법으로 나타난 숫자를 B진법으로 변환해야 한다.
    
    # 먼저 10진수로 변환한다.
    value = 0
    for i, n in enumerate(nums, start = 1):
        value += n * pow(A, len(nums) - i)
    
    # 10진수로 변환한 것을 B진법으로 변환한다.
    B_nums = []
    while value != 0:
        a, b = value // B, value % B
        B_nums.append(b)
        value = a
    print(*B_nums[::-1])
        
 
solution()