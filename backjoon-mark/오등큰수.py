def solution():
    from collections import Counter

    N = int(input())
    Array = list(map(int, input().split()))
    counter = Counter(Array)
    stack = []
    answer = [-1] * N
    for i, a in enumerate(Array):
        while stack and stack[-1][1] < counter[a]:
            idx, count = stack.pop()
            answer[idx] = a
        stack.append((i, counter[a]))
    print(*answer)

solution()