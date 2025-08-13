import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

# 상어가 하나도 없는 경우 바로 0을 출력하고 종료
if M == 0:
    print(0)
    sys.exit()

# 상어 정보를 저장할 딕셔너리
#  - key: (r, c)  (상어의 행, 열 위치)
#  - value: (s, d, z)  (상어의 속력, 방향, 크기)
sharks = {}

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r, c)] = (s, d, z)


# 방향 정의 (문제에서 주어지는 값)
# 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
# 이동을 계산할 때 편의를 위해 벡터를 직접 쓰기보다는
# 아래 move_shark 함수에서 ‘mod + bounce’ 방식을 사용
def move_shark(r, c, s, d):
    """
    (r, c)에서 (속력=s, 방향=d)인 상어를
    1회 이동시켰을 때의 (새로운 r, 새로운 c, 새로운 d)를 반환하는 함수.
    여기서는 매 스텝마다 한 칸씩 이동하는 대신,
    'mod + bounce' 기법을 써서 O(1)에 계산합니다.
    """
    # 1 또는 2인 경우(위, 아래)
    if d == 1 or d == 2:
        # 세로 이동의 총 주기 = (R - 1) * 2
        cycle = 2 * (R - 1)

        # 만약 R이 1이라면, 세로 이동 자체가 불가능
        if R == 1:
            return (r, c, d)

        # 속력을 주기로 나눈 나머지만큼만 실제로 이동
        s %= cycle

        # 편의를 위해 위치 r을 0-based로 변환
        pos = r - 1

        # 방향에 따른 이동 부호
        # d=1(위)이면 dir_sign=-1, d=2(아래)이면 dir_sign=+1
        dir_sign = -1 if d == 1 else 1

        # pos를 s만큼 이동
        pos += dir_sign * s

        # 범위를 벗어나면 "바운스(bounce)" 처리
        # pos < 0 또는 pos >= (R-1)인 경우에 대해 반사
        if pos < 0:
            pos = -pos
            dir_sign *= -1
        elif pos >= (R - 1):
            pos = 2 * (R - 1) - pos
            dir_sign *= -1

        # 다시 한 번 경계 검사(주기와 정확히 일치하는 경우 등)
        if pos < 0:
            pos = -pos
            dir_sign *= -1
        elif pos >= (R - 1):
            pos = 2 * (R - 1) - pos
            dir_sign *= -1

        # pos(0-based)를 다시 1-based 좌표로 변환
        new_r = pos + 1

        # 방향 갱신
        # dir_sign이 -1이면 위쪽(1), +1이면 아래쪽(2)
        new_d = 1 if dir_sign == -1 else 2
        return (new_r, c, new_d)

    else:
        # d == 3 or d == 4 (오른쪽, 왼쪽)
        cycle = 2 * (C - 1)

        # 만약 C가 1이라면, 가로 이동 자체가 불가능
        if C == 1:
            return (r, c, d)

        s %= cycle
        pos = c - 1

        # 방향에 따른 이동 부호
        # d=4(왼쪽) -> dir_sign=-1, d=3(오른쪽) -> dir_sign=+1
        dir_sign = -1 if d == 4 else 1

        # pos 이동
        pos += dir_sign * s

        # 바운스 처리 (왼쪽/오른쪽 경계)
        if pos < 0:
            pos = -pos
            dir_sign *= -1
        elif pos >= (C - 1):
            pos = 2 * (C - 1) - pos
            dir_sign *= -1

        # 다시 한 번 경계 검사
        if pos < 0:
            pos = -pos
            dir_sign *= -1
        elif pos >= (C - 1):
            pos = 2 * (C - 1) - pos
            dir_sign *= -1

        new_c = pos + 1
        # 방향 갱신
        # dir_sign이 -1이면 왼쪽(4), +1이면 오른쪽(3)
        new_d = 4 if dir_sign == -1 else 3
        return (r, new_c, new_d)


answer = 0

# 낚시왕이 왼쪽 열부터 오른쪽 열까지 한 칸씩 이동
for col in range(1, C + 1):
    # 1) 현재 col 열에서 가장 가까운(행 번호가 가장 작은) 상어를 잡음
    catch_row = None
    catch_size = 0

    for (r, c), (s, d, z) in sharks.items():
        if c == col:
            # 제일 위(행 번호가 작은) 상어 찾기
            if catch_row is None or r < catch_row:
                catch_row = r
                catch_size = z

    # 잡을 상어가 있다면 잡아서 점수(answer)에 추가하고, 해당 상어는 제거
    if catch_row is not None:
        answer += catch_size
        del sharks[(catch_row, col)]

    # 2) 모든 상어를 이동
    new_sharks = {}
    for (r, c), (s, d, z) in sharks.items():
        new_r, new_c, new_d = move_shark(r, c, s, d)

        # 이동 후 위치가 (new_r, new_c)인 상어가 이미 있다면,
        # 크기가 더 큰 상어만 살아남도록 처리
        if (new_r, new_c) in new_sharks:
            old_s, old_d, old_z = new_sharks[(new_r, new_c)]
            if old_z < z:
                new_sharks[(new_r, new_c)] = (s, new_d, z)
        else:
            new_sharks[(new_r, new_c)] = (s, new_d, z)

    # 이동이 모두 끝난 뒤 결과를 sharks에 갱신
    sharks = new_sharks

# 최종적으로 잡은 상어 크기의 합
print(answer)
