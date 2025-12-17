def solution(A):
    A.sort()
    stack = []
    for num in A:
        if stack and 0 <= stack[-1] < num and stack[-1] + 1 != num:  # [-100, 3, 4] 이런 경우를 체크하지 못한다...
            return stack[-1] + 1
        stack.append(num)

    # 모든 경우에 대응하여 스택이 비어있거나 마지막 값이 음수일 때 1을 반환
    return stack[-1] + 1 if stack and stack[-1] >= 0 else 1


def solution2(A):
    A.sort()
    smallest = 1
    for i in range(len(A)):
        if smallest == A[i]:
            smallest += 1
    return smallest