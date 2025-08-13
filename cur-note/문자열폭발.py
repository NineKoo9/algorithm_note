def solution():
    Array = input()
    bomb = list(input())
    bomb_len = len(bomb)
    stack = []
    for ch in Array:
        stack.append(ch)
        while len(stack) >= bomb_len and stack[-bomb_len:] == bomb:
            for _ in range(bomb_len):
                stack.pop()
    if stack:
        print("".join(stack))
    else:
        print("FRULA")


def solution2():
    phrase = input()
    explode_word = input()
    explode_len = len(explode_word)
    stack = []

    for ch in phrase:
        stack.append(ch)
        while len(stack) >= explode_len and all(stack[-i] == explode_word[-i] for i in range(1, explode_len+1)):
            # stack = stack[-explode_len:] 이것보다는 아래것이 더 시간복잡도가 낮구나...?
            for _ in range(explode_len):
                stack.pop()
    print("".join(stack) if stack else "FRULA")


solution2()
# 시간초과가 발생하네...?
# 와 String += String 은 시간복잡도가 N^2 이 되겠네