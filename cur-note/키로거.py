def solution():
    def find_password(input:str) -> str:
        stack1 = [] # 커서는 이녀석 제일 위에 있다고 생각하자.
        stack2 = []
        for c in input:
            if c.isalpha() or c.isnumeric():
                stack1.append(c)
            elif c == "<":
                if not stack1:
                    continue
                stack2.append(stack1.pop())
            elif c == ">":
                if not stack2:
                    continue
                stack1.append(stack2.pop())
            else: # 이 경우는 백스페이스겠지?
                if not stack1:
                    continue
                stack1.pop()
        return "".join(stack1 + stack2[::-1])
    
    
    N = int(input())
    test_cases = [input() for _ in range(N)] # 각 케이스는 100만이하
    answers = []
    for test_case in test_cases:
        print(find_password(test_case))

solution()