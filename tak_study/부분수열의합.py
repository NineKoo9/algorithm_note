count = 0
def solution():
    global count

    def recur(cur, cur_sum, path):
        global count

        if cur == N and cur_sum == S and len(path) > 0:
            count += 1
            return
        if cur == N:
            return

        recur(cur + 1, cur_sum + numbers[cur], path + [numbers[cur]])
        recur(cur + 1, cur_sum, path)

    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    recur(0, 0, [])
    print(count)

solution()