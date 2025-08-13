from typing import Tuple


def solution():
    def find_seat(*prefer_friends):
        table_cond_info = []
        for y in range(N):
            for x in range(N):
                # 현 위치가 비어있지않다면 제외
                if table[y][x] != 0:
                    continue
                # 각 칸마다 인접한 칸들을 확인한다. 현 위치에서 인접한 칸에 비어있는 녀석은 몇개인지, 좋아하는 녀석은 몇명인지 판단한다.
                prefer_count, empty_count = 0, 0
                for i in range(4):
                    # 테이블범위를 넘어가면 제외
                    n_y = y + dy[i]
                    n_x = x + dx[i]
                    if not (0 <= n_y < N and 0 <= n_x < N):
                        continue
                    # 인접한 칸이 비어있다면 카운팅해준다.
                    if table[n_y][n_x] == 0:
                        empty_count += 1
                        continue
                    # 인접한 칸에 좋아하는 사람이 있다면 카운팅해준다.
                    if table[n_y][n_x] in prefer_friends:
                        prefer_count += 1
                table_cond_info.append((prefer_count, empty_count, y, x)) # 좋아하는 사람이 몇명인지, 빈자리는 몇명인지 현위치 정보 저장
        table_cond_info.sort(key=lambda info:(-info[0], -info[1], info[2], info[3]))
        # 정렬을 했는데... 여기서 어떻게 한 자리를 정하지? 기본적으로 400개가 정렬이 되었을 것이다. 그렇지.. 제일 첫 녀석이 이것을 만족하는 녀석이겠지
        return (table_cond_info[0][2], table_cond_info[0][3])
    
    N = int(input())
    prefer_infos = [list(map(int, input().split())) for _ in range(N**2)]
    prefer_infos_dic = {}
    table = [[0] * N for _ in range(N)] # N * N 테이블의 자리배치를 기록한다.
    score_dic = {0:0, 1:1, 2:10, 3:100, 4:1000}
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 먼저 학생 한명한명 자리를 정해나가야겠다.
    for s, f1, f2, f3, f4 in prefer_infos: # 최대 400 이다.
        prefer_infos_dic[s] = (f1, f2, f3, f4)
        # 여기서 table을 모두 탐색할까? 그리고 4방향도 모두 탐색? 그러면 최대 1600이다. 400 * 1600 = 640000 이면 할만한데?
        y, x = find_seat(f1, f2, f3, f4)
        table[y][x] = s
    total_score = 0
    for y in range(N):
        for x in range(N):
            s = table[y][x]
            count = 0
            # 인접한 테이블을 확인한다.
            for i in range(4):
                n_y = y + dy[i]
                n_x = x + dx[i]
                if not (0 <= n_y < N and 0 <= n_x < N):
                    continue
                if table[n_y][n_x] in prefer_infos_dic[s]:
                    count += 1
            total_score += score_dic[count]
    print(total_score)
    
def solution2():
    from functools import cmp_to_key
    def get_table_point(s) -> tuple[int, int]:
        def compare(point1, point2) -> int:
            # 먼저 인접한 칸에 좋아하는 사람이 몇명인지 체크한다.
            point1_count, point2_count = 0, 0
            for i in range(4):
                n_point1_y = point1[0] + dy[i]
                n_point1_x = point1[1] + dx[i]
                n_point2_y = point2[0] + dy[i]
                n_point2_x = point2[1] + dx[i]
                point1_count += 1 if 0 <= n_point1_y < N and 0 <= n_point1_x < N and table[n_point1_y][n_point1_x] in prefer_person[s] else 0
                point2_count += 1 if 0 <= n_point2_y < N and 0 <= n_point2_x < N and table[n_point2_y][n_point2_x] in prefer_person[s] else 0
            if point1_count > point2_count:  # 많은 녀석이 앞에 와야한다.즉 일반적인 경우의 역순이다.
                return -1
            elif point1_count < point2_count:
                return 1
            else: # 이제 같은 경우니까... 비어있는 칸이 가장 많은 것을 체크해야지?
                empty_count1, empty_count2 = 0, 0
                for i in range(4):
                    n_point1_y = point1[0] + dy[i]
                    n_point1_x = point1[1] + dx[i]
                    n_point2_y = point2[0] + dy[i]
                    n_point2_x = point2[1] + dx[i]
                    empty_count1 += 1 if 0 <= n_point1_y < N and 0 <= n_point1_x < N and table[n_point1_y][n_point1_x] == 0 else 0
                    empty_count2 += 1 if 0 <= n_point2_y < N and 0 <= n_point2_x < N and table[n_point2_y][n_point2_x] == 0 else 0
                if empty_count1 > empty_count2:
                    return -1
                elif empty_count1 < empty_count2:
                    return 1
                else:
                    if point1[0] < point2[0]: # 여기서 행을 비교하는데 더 작은 녀석이 앞에 와야한다.
                        return -1
                    elif point1[0] > point2[0]:
                        return 1
                    else:
                        return point1[1] - point2[1]
        table_points = [(i, j) for j in range(N) for i in range(N) if table[i][j] == 0]
        table_points.sort(key=cmp_to_key(compare))
        print(table_points)
        return table_points[0]

    N = int(input())
    infos = [tuple(map(int, input().split())) for _ in range(N * N)]
    # 어쨋든 만족도를 구해야하는데... N 은 최대 20이니까 칸은 400 개가 최대다.
    prefer_person = {s: persons for s, *persons in infos}
    table = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for info in infos:
        s = info[0]
        i, j = get_table_point(s)
        print(s, i, j)
        table[i][j] = s
    print(table)
    result = 0
    for y in range(N):
        for x in range(N):
            stud = table[y][x]
            count = 0
            for i in range(4):
                n_y = y + dy[i]
                n_x = x + dx[i]
                count += 1 if 0 <= n_y < N and 0 <= n_x < N and table[n_y][n_x] in prefer_person[stud] else 0
            if count == 1:
                result += 1
            elif count == 2:
                result += 10
            elif count == 3:
                result += 100
            elif count == 4:
                result += 1000


    print(result)


from functools import cmp_to_key
import sys

def solution3():
    def get_table_point(s) -> tuple[int, int]:
        def compare(point1, point2) -> int:
            # 먼저 인접한 칸에 좋아하는 사람이 몇명인지 체크한다.
            point1_count, point2_count = 0, 0
            for i in range(4):
                n_point1_y = point1[0] + dy[i]
                n_point1_x = point1[1] + dx[i]
                n_point2_y = point2[0] + dy[i]
                n_point2_x = point2[1] + dx[i]
                if 0 <= n_point1_y < N and 0 <= n_point1_x < N and table[n_point1_y][n_point1_x] in prefer_person[s]:
                    point1_count += 1
                if 0 <= n_point2_y < N and 0 <= n_point2_x < N and table[n_point2_y][n_point2_x] in prefer_person[s]:
                    point2_count += 1

            if point1_count != point2_count:
                return point2_count - point1_count  # 많은 녀석이 앞에 와야 한다.

            # 이제 같은 경우니까 비어있는 칸이 가장 많은 것을 체크해야지
            empty_count1, empty_count2 = 0, 0
            for i in range(4):
                n_point1_y = point1[0] + dy[i]
                n_point1_x = point1[1] + dx[i]
                n_point2_y = point2[0] + dy[i]
                n_point2_x = point2[1] + dx[i]
                if 0 <= n_point1_y < N and 0 <= n_point1_x < N and table[n_point1_y][n_point1_x] == 0:
                    empty_count1 += 1
                if 0 <= n_point2_y < N and 0 <= n_point2_x < N and table[n_point2_y][n_point2_x] == 0:
                    empty_count2 += 1

            if empty_count1 != empty_count2:
                return empty_count2 - empty_count1

            # 행을 비교하는데 더 작은 녀석이 앞에 와야 한다.
            if point1[0] != point2[0]:
                return point1[0] - point2[0]

            # 열을 비교한다.
            return point1[1] - point2[1]

        table_points = [(i, j) for i in range(N) for j in range(N) if table[i][j] == 0]
        table_points.sort(key=cmp_to_key(compare))
        return table_points[0]

    N = int(sys.stdin.readline())
    infos = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N * N)]
    prefer_person = {s: persons for s, *persons in infos}
    table = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for info in infos:
        s = info[0]
        i, j = get_table_point(s)
        table[i][j] = s

    result = 0
    for y in range(N):
        for x in range(N):
            stud = table[y][x]
            count = 0
            for i in range(4):
                n_y = y + dy[i]
                n_x = x + dx[i]
                if 0 <= n_y < N and 0 <= n_x < N and table[n_y][n_x] in prefer_person[stud]:
                    count += 1
            if count == 1:
                result += 1
            elif count == 2:
                result += 10
            elif count == 3:
                result += 100
            elif count == 4:
                result += 1000

    print(result)

def solution4():
    def get_empty_places(my_friends):
        result = []
        for y in range(N):
            for x in range(N):
                # 자 이제 비어있는 (i, j)에서 주위의 칸을 탐색해야한다.
                if board[y][x] != 0:
                    continue
                f_count, e_count = 0, 0
                for i in range(4):
                    n_y, n_x = y + dy[i], x + dx[i]
                    if not (0 <= n_y < N and 0 <= n_x < N):
                        continue
                    if board[n_y][n_x] == 0:
                        e_count += 1
                    if board[n_y][n_x] in my_friends:
                        f_count += 1
                result.append((f_count, e_count, y, x))
        return result

    N = int(input())
    friends = {a: {b, c, d, e} for a, b, c, d, e in (map(int, input().split()) for _ in range(N * N))}
    dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
    board = [[0] * N for _ in range(N)]
    for student in friends.keys():
        empty_places = get_empty_places(friends[student])
        empty_places.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
        _, _, y, x = empty_places[0]
        board[y][x] = student
    # 이제 만족도를 구해야한다.
    total_satisfy_point = 0
    for y in range(N):
        for x in range(N):
            s = board[y][x]
            # 이제 s주위에 친구가 몇명 있는지 확인한다.
            f_count = 0
            for i in range(4):
                n_y, n_x = y + dy[i], x + dx[i]
                if not (0 <= n_y < N and 0 <= n_x < N):
                    continue
                if board[n_y][n_x] in friends[s]:
                    f_count += 1
            satisfy_point = 0
            if f_count == 1:
                satisfy_point = 1
            elif f_count == 2:
                satisfy_point = 10
            elif f_count == 3:
                satisfy_point = 100
            elif f_count == 4:
                satisfy_point = 1000
            total_satisfy_point += satisfy_point
    print(total_satisfy_point)


solution4()