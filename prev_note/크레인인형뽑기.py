def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            c = board[i][move-1]
            if c == 0:
                continue
            board[i][move-1] = 0
            if stack and stack[-1] == c:
                answer += 2
                stack.pop()
            else:
                stack.append(c)
            break
    print(stack)
    return answer