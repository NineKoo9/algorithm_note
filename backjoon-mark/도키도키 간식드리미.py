def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    stack = []
    answer = []
    for num in nums:
        # 그러니까 스택을 이용해서 nums 을 정렬할 수 있느냐가 문제구나?
        while stack and stack[-1] < num:
            answer.append(stack.pop())
        stack.append(num)
    answer += stack[::-1]
    print("Nice" if answer == [i for i in range(1, N+1)] else "Sad")
    
solution()