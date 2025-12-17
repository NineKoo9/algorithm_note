min_diff = int(1e9)

def solution():
    global min_diff
    def calc_color_dist(tar, combi):
        return abs(tar[0] - combi[0]) + abs(tar[1] - combi[1]) + abs(tar[2] - combi[2])

    def calc_color(lst):
        r, g, b = 0, 0, 0
        for i in lst:
            r += rgb_lst[i][0]
            g += rgb_lst[i][1]
            b += rgb_lst[i][2]
        l = len(lst)
        return r//l, g//l, b//l

    def recur(cur, path):
        global min_diff

        if cur == N:
            if len(path) < 2:
                return
            cur_color = calc_color(path)
            color_dist = calc_color_dist(target, cur_color)
            min_diff = min(min_diff, color_dist)
            return

        if len(path) < 7:
            recur(cur + 1, path + [cur])
        recur(cur + 1, path)


    N = int(input())
    rgb_lst = [list(map(int, input().split())) for _ in range(N)]
    target = list(map(int, input().split()))
    recur(0, [])
    print(min_diff)

solution()