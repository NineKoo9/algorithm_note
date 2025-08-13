def solution():
    def check(s):
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
            
    
    T = int(input())
    cases = [input() for _ in range(T)]
    for case in cases:
        if check(case):
            print("YES")
        else:
            print("NO")
            
solution()