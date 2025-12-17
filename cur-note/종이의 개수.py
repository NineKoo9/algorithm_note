from collections import defaultdict

def solution():
    def div_conq(y, x, size):
        if size == 1:
            paper_count[M[y][x]] += 1
            return M[y][x] # size가 1이 되면 그 좌표의 -1, 0, 1의 값을 리턴한다.
        size = size // 3
        result = defaultdict(int)
        for i in range(3):
            for j in range(3):
                r = div_conq(y + size * i, x + size * j, size)
                if r is not None:
                    result[r] += 1
        keys = list(result.keys())
        if len(keys) == 1 and result[keys[0]] == 9: # 모두 똑같다면? 갯수를 세어주었던 것을 다시 빼준다. 그리고 하나로 넘긴다.
            key = keys[0]
            paper_count[key] -= 8
            return key
        
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    paper_count = [0, 0, 0]
    div_conq(0, 0, N)
    print(paper_count[-1], paper_count[0], paper_count[1], sep="\n")

def solution2():
    def div_and_conquer(y, x, cur_size):
        if cur_size == 1:
            return M[y][x]

        div_size = cur_size // 3
        results = []
        for i in range(3):
            for j in range(3):
                n_y = y + div_size * i
                n_x = x + div_size * j
                results.append(div_and_conquer(n_y, n_x, div_size))
        if None not in results and all(results[0] == result for result in results):
            return results[0]
        else:
            for result in results:
                if result is None:
                    continue
                paper_count[result] += 1
            return None

    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    paper_count = {-1: 0, 0: 0, 1: 0}
    result = div_and_conquer(0, 0, N)
    if result is not None:
        paper_count[result] += 1
    print(paper_count[-1], paper_count[0], paper_count[1], sep="\n")


minus_one_count = 0
zero_count = 0
one_count = 0
def solution3():
    global minus_one_count, zero_count, one_count

    def check(size, y, x):
        s = set()
        for i in range(size):
            for j in range(size):
                s.add(matrix[y + i][x + j])
        if len(s) == 1:
            return True
        else: return False

    def dfs(size, y, x):
        global minus_one_count, zero_count, one_count

        if check(size, y, x):
            number = matrix[y][x]
            if number == 1:
                one_count += 1
            elif number == 0:
                zero_count += 1
            else:
                minus_one_count += 1
            return

        next_size = size // 3
        for i in range(3):
            for j in range(3):
                n_y = y + next_size * i
                n_x = x + next_size * j
                dfs(next_size, n_y, n_x)

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]  # 크기는 최대 478만이다.
    dfs(N, 0, 0)
    print(minus_one_count)
    print(zero_count)
    print(one_count)

solution3()