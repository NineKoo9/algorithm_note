# def get_zero_count(y, x):
#     count = 0
#     for i in range(9):
#         if i == y:
#             continue
#         if table[i][x] == 0:
#             count += 1
#     for i in range(9):
#         if i == x:
#             continue
#         if table[y][i] == 0:
#             count += 1
#     # 속한 네모모양 칸에 0이 있는지 살펴보자.
#     middle_y, middle_x = 3 * (y // 3) + 1, 3 * (x // 3) + 1
#     for i in range(8):
#         if y == middle_y + d_y[i] and x == middle_x + d_x[i]:
#             continue
#         if table[middle_y + d_y[i]][middle_x + d_x[i]] == 0:
#             count += 1
#     return count
#
# def check(y, x, num):
#     for i in range(9):
#         if x == i:
#             continue
#         if table[y][i] == num:
#             return False
#     for i in range(9):
#         if y == i:
#             continue
#         if table[i][x] == num:
#             return False
#     middle_y, middle_x = 3 * (y // 3) + 1, 3 * (x // 3) + 1
#     for i in range(9):
#         if y == middle_y + d_y[i] and x == middle_x + d_x[i]:
#             continue
#         if table[middle_y + d_y[i]][middle_x + d_x[i]] == num:
#             return False
#     return True
#
# def sudoku(n):
#     if n == len(zero_points):
#         for row in table:
#             print(*row)
#         exit() # 여기서 exit 하지 않으면.. 함수 빠져 나오고 다시 탐색이 이루어지는데...
#     for num in range(1, 10):
#         y, x, _ = zero_points[n]
#         if check(y, x, num):
#             table[y][x] = num
#             sudoku(n + 1)
#             table[y][x] = 0
#
    
# table = [list(map(int, input().split())) for _ in range(9)]
# d_y = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# d_x = [0, 0, 1, 1, 1, 0, -1, -1, -1]
# zero_points = []
# for y, row in enumerate(table):
#     for x, num in enumerate(row):
#         if num != 0:
#             continue
#         # 여기서 후보가 몇개가 가능한지 함께 기록하자.
#         count = get_zero_count(y, x)
#         zero_points.append((y, x, count))
# zero_points.sort(key=lambda point:point[2])
# sudoku(0) # 이 녀석과 퀸 문제와 비슷한 것을 볼수있어야하는데...

# def check_sudoku(y, x):
#     if M[y][x] in [M[y][xi] for xi in range(9) if xi != x]:
#         return False
#     if M[y][x] in [M[yi][x] for yi in range(9) if yi != y]:
#         return False
#     # 자 이제... 사각형인데.. 흠...
#     m_x = 3 * (x // 3) + 1
#     m_y = 3 * (y // 3) + 1
#     if M[y][x] in [M[m_y + d_y[i]][m_x + d_x[i]] for i in range(9) if (m_y + d_y[i]) != y and (m_x + d_x[i]) != x]:
#         return False
#     return True
#
# def dfs(sub_zero_points):
#     if len(sub_zero_points) == 0:
#         for row in M:
#             print(*row)
#         exit()
#     cur_point = sub_zero_points.pop()
#     y = cur_point[0]
#     x = cur_point[1]
#     # 중복된 수만 아니면 괜찮다고 하자
#     for i in range(1, 10):
#         M[y][x] = i
#         if check_sudoku(y, x):
#             dfs(sub_zero_points.copy())
#         M[y][x] = 0
#
# M = [list(map(int, input().split())) for _ in range(9)]
# d_y = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# d_x = [0, 0, 1, 1, 1, 0, -1, -1, -1]
# # 어떻게 풀까?
# zero_points = []
# zero_count = 0
# for i in range(9):
#     for j in range(9):
#         if M[i][j] == 0:
#             zero_points.append((i, j))
#             zero_count += 1
# dfs(zero_points)
# # 2번째 방법이 오래걸린 이유는... 매번 리스트를 가지고 재귀를 탐색하기 때문이야... 인덱스로하면 더 간단한건데 굳이...


def solution():
    def is_ok(y, x, value):
        # 먼저 포함된 사각형을 따져보자.
        middle_point_y, middle_point_x = (y // 3) * 3 + 1, (x // 3) * 3 + 1
        for i in range(9):
            n_y = middle_point_y + dy[i]
            n_x = middle_point_x + dx[i]
            if y == n_y and x == n_x:
                continue
            if table[n_y][n_x] == value:
                return False

        # 이제 가로 값을 살펴보자
        if value in {table[y][i] for i in range(9) if (y, i) != (y, x)}:
            return False

        # 이제 세로 값을 살펴보자
        if value in {table[j][x] for j in range(9) if (j, x) != (y, x)}:
            return False

        return True

    def dfs(zero_point_idx):
        if zero_point_idx == len(zero_points):
            for row in table:
                print("".join(row))
            exit()

        # for i in range(zero_point_idx, len(zero_points)):
        y, x = zero_points[zero_point_idx]
        for number in numbers:
            if not is_ok(y, x, number):
                continue
            table[y][x] = number
            dfs(zero_point_idx + 1)
            table[y][x] = "0"

    table = [list(input()) for _ in range(9)]

    dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    zero_points = [(i, j) for i in range(9) for j in range(9) if table[i][j] == "0"]
    dfs(0)

# 이거는 gpt가 짜준 것인데... 미리 행 렬 박스를 만들어두고 넣었다가 뺐다가 반복하는 것이 훨씬 빠르구나? 이렇게 하면 o(1)의 속도로 유효성 검사가 가능해
def solution2():
    import sys

    # 표 입력 받기
    table = [list(sys.stdin.readline().strip()) for _ in range(9)]

    # 행, 열, 3x3 박스에 이미 어떤 숫자들이 있는지 기록할 집합(Set) 준비
    # rows[r] = r번째 행에 이미 들어 있는 숫자들의 집합
    # cols[c] = c번째 열에 이미 들어 있는 숫자들의 집합
    # boxes[b] = b번째 박스(0~8)에 이미 들어 있는 숫자들의 집합
    #    b = (r // 3) * 3 + (c // 3)  => 3x3 박스를 0~8로 인덱싱
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # 0(빈 칸)의 위치들을 모아두기
    zero_points = []

    # 초기 테이블 정보를 이용해 rows, cols, boxes 세팅
    for r in range(9):
        for c in range(9):
            val = table[r][c]
            if val != '0':
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + (c // 3)].add(val)
            else:
                zero_points.append((r, c))

    def dfs(idx):
        # 모든 빈칸을 채웠다면 결과 출력 후 종료
        if idx == len(zero_points):
            for row in table:
                print("".join(row))
            sys.exit(0)  # 혹은 return

        r, c = zero_points[idx]
        b = (r // 3) * 3 + (c // 3)  # 박스 인덱스

        # 1~9 숫자를 대입 시도
        for num in map(str, range(1, 10)):
            # 이미 같은 행, 열, 박스에 num이 있으면 건너뜀
            if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                # 숫자 배치
                table[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

                # 다음 빈칸 탐색
                dfs(idx + 1)

                # 배치했던 숫자 되돌리기(백트래킹)
                table[r][c] = '0'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)

    dfs(0)


solution2()