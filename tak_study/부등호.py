min_status, max_status = False, False

def solution():
    def find_min(cur):
        global min_status
        if cur == k + 1:
            print("".join(map(str, selected)))
            min_status = True
            return

        for n in range(10):
            if visited[n] or min_status == True:
                continue
            if cur > 0:
                if sign[cur - 1] == "<" and selected[cur - 1] > n:
                    continue
                elif sign[cur - 1] == ">" and selected[cur - 1] < n:
                    continue

            visited[n] = 1
            selected[cur] = n
            find_min(cur + 1)
            visited[n] = 0

    def find_max(cur):
        global max_status

        if cur == k + 1:
            print("".join(map(str, selected)))
            max_status = True
            return

        for n in range(9, -1, -1):
            if visited[n] or max_status == True:
                continue
            if cur > 0:
                if sign[cur - 1] == "<" and selected[cur - 1] > n:
                    continue
                elif sign[cur - 1] == ">" and selected[cur - 1] < n:
                    continue

            visited[n] = 1
            selected[cur] = n
            find_max(cur + 1)
            visited[n] = 0

    k = int(input())
    sign = list(input().split())
    selected = [0] * (k + 1)
    visited = [0] * 10
    find_max(0)
    find_min(0)

solution()