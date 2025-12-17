max_value = 0

def solution():
    global max_value
    def recur(cur, cur_value):
        global max_value
        if cur == N:
            max_value = max(max_value, cur_value)
            return
        elif cur > N:
            return

        # 선택하는 경우
        next_value = cur_value + meetings[cur][1]
        next_cur = cur + meetings[cur][0]
        recur(next_cur, next_value)

        # 선택하지 않는 경우
        recur(cur + 1, cur_value)


    N = int(input())
    meetings = [list(map(int, input().split())) for _ in range(N)]
    recur(0, 0)
    print(max_value)

solution()