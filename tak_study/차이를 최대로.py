max_value = -int(1e9)

def solution():
    global max_value
    def calc(lst):
        result = 0
        for i in range(len(lst) - 1):
            result += abs(lst[i] - lst[i + 1])
        return result

    def recur(cur):
        global max_value
        if cur == N:
            calculated_result = calc(selected)
            max_value = max(max_value, calculated_result)
            return
        for i in range(N):
            n = A[i]
            if visited[i]:
                continue
            visited[i] = 1
            selected[cur] = n
            recur(cur + 1)
            visited[i] = 0

    N = int(input())
    A = list(map(int, input().split()))
    selected = [0] * N
    visited = [0] * N
    recur(0)
    print(max_value)


solution()