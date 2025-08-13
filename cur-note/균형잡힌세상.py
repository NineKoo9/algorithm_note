def solution():
    def check(p) -> bool:
        stack = []
        for ch in p:
            if ch == "[" or ch == "(":
                stack.append(ch)
            elif ch == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif ch == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
    
    phrases = []
    while 1:
        phrase = input()
        if phrase == ".":
            break
        phrases.append(phrase)
    for phrase in phrases:
        if check(phrase):
            print("yes")
        else:
            print("no")
    
solution()