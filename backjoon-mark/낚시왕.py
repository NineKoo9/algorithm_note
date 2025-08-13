def catch_shark(fisher):
    result = 0
    for i in range(R + 1):
        if shark_board[i][fisher] and shark_board[i][fisher][0] > 0:
            result = shark_board[i][fisher][0]
            # 잡았으니까 각 값을 제거해주는 것이 맞다.
            shark_board[i][fisher].remove(result)
            del shark_point[result]
            return result
    return result

def move(sha, spe):
    y, x = shark_point[sha]
    # 기존의 위치에서 제거한다.
    shark_board[y][x].remove(sha)

    # 이제부터 이동한 위치를 구해야한다.
    # 시작지점을 0으로 해야 올바른 모듈로연산이 된다. 안그러면 덧셈 해야함
    d = shark_direction[sha]
    if d == 1 or d == 2: #위 아래
        cycle = 2 * (R - 1)
        pos = y
        dir_sign = -1 if d == 1 else 1
        pos += dir_sign * (spe % cycle)
        if pos < 1:
            pos = 1 + (1 - pos)
            dir_sign *= -1
        elif pos >= R:
            pos = R - (pos - R)
            dir_sign *= -1
        # 한번더 처리
        if pos < 1:
            pos = 1 + (1 - pos)
            dir_sign *= -1
        elif pos >= R:
            pos = R - (pos - R)
            dir_sign *= -1
        y = pos
        new_d = 1 if dir_sign == -1 else 2
    else:  # 오른쪽 왼쪽
        cycle = 2 * (C - 1)
        pos = x
        dir_sign = 1 if d == 3 else -1
        pos += dir_sign * (spe % cycle)
        if pos < 1:
            pos = 1 + (1 - pos)
            dir_sign *= -1
        elif pos >= C:
            pos = C - (pos - C)
            dir_sign *= -1
        # 한번 더 처리한다.
        if pos < 1:
            pos = 1 + (1 - pos)
            dir_sign *= -1
        elif pos >= C:
            pos = C - (pos - C)
            dir_sign *= -1
        x = pos
        new_d = 3 if dir_sign == +1 else 4

    shark_board[y][x].append(sha)
    shark_point[sha] = [y, x]
    shark_direction[sha] = new_d

def remove_double():
    for i in range(R + 1):
        for j in range(C + 1):
            if len(shark_board[i][j]) > 1:
                shark_board[i][j].sort(reverse = True)
                while len(shark_board[i][j]) > 1:
                    small_shark = shark_board[i][j].pop()
                    # 이제 이 녀석의 정보를 제거해야한다.
                    del shark_point[small_shark]

R, C, M = map(int, input().split())
shark_info = [map(int, input().split()) for _ in range(M)]


# 각 상어는 크기로 구분하자
shark_direction, shark_point, shark_speed = {}, {}, {}
shark_board = [[[] for _ in range(C + 1)] for _ in range(R + 1)] # 각 좌표에 상어식별값(사이즈)가 저장되어 있다.
# 이 모든 것을 board을 만들고 체크할 필요가 있을까? 흠... 그냥... 좌표 x 좌표만 탐색하면 되지 않나?
for r, c, s, d, size in shark_info:
    shark_direction[size] = d
    shark_speed[size] = s
    shark_point[size] = [r, c]
    shark_board[r][c].append(size)

total_shark, fisher_point = 0, 0
for _ in range(C):
    fisher_point += 1
    total_shark += catch_shark(fisher_point)
    for shark in shark_point.keys():
        speed= shark_speed[shark]
        move(shark, speed) # 한가지 주의할 점이 같은 칸에 있으면 작은 녀석은 사라진다.
    remove_double()

print(total_shark)