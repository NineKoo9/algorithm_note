count = 0
def solution():
    global count

    def recur(cur, cur_sum, path):
        global count
        if cur == N and L <= cur_sum <= R and path[-1] - path[0] >= X:
            count += 1
            return
        if cur == N:
            return

        recur(cur + 1, cur_sum + A[cur], path + [A[cur]])
        recur(cur + 1, cur_sum, path)

    N, L, R, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    recur(0, 0, [])
    print(count)

solution()