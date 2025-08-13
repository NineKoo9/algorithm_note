import sys

sys.setrecursionlimit(10 ** 8)

input = lambda: sys.stdin.readline().rstrip()


def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def upper_bound(up_diag_idx, n, board, used_down_diag):
    """
    현재 우상향 대각선 up_diag_idx부터 끝까지 훑어보며,
    각 우상향 대각선에서 '놓을 수 있는 칸이 단 하나라도 존재'한다면
    개수를 센다(가능성 있는 대각선 수).
    """
    max_possible = 0
    # 우상향 대각선은 0부터 2*n - 2까지 가능
    for d in range(up_diag_idx, 2 * n - 1):
        # 우상향 대각선 d에 포함되는 (y, x) 쌍은 y + x = d 형태
        # 하지만 코드에서는 for y in range(d+1): x = d-y 로 순회
        for y in range(d + 1):
            x = d - y
            if in_range(y, x, n) and board[y][x] == 1 and used_down_diag[x - y] == 0:
                max_possible += 1
                break
    return max_possible


def backtrack(up_diag_idx, count_bishops, n, board, used_down_diag, best):
    """
    up_diag_idx   : 현재 확인할 우상향 대각선의 인덱스 (0 ~ 2*n - 2)
    count_bishops : 현재까지 놓인 비숍의 수
    best          : [현재까지 구한 최적해]를 저장하는 리스트 혹은 전역 변수
    """
    if up_diag_idx == 2 * n:
        # 모든 우상향 대각선을 검사 끝냈다면
        best[0] = max(best[0], count_bishops)
        return

    # 가지치기를 위한 상한 계산
    ub = upper_bound(up_diag_idx, n, board, used_down_diag)
    if count_bishops + ub <= best[0]:
        return

    # 현재 우상향 대각선에 속하는 모든 칸 탐색
    for y in range(up_diag_idx + 1):
        x = up_diag_idx - y
        if in_range(y, x, n) and board[y][x] == 1 and used_down_diag[x - y] == 0:
            # (y, x)에 비숍 놓기
            used_down_diag[x - y] = 1
            backtrack(up_diag_idx + 1, count_bishops + 1, n, board, used_down_diag, best)
            used_down_diag[x - y] = 0

    # (y, x)에 비숍 안 놓는 경우
    backtrack(up_diag_idx + 1, count_bishops, n, board, used_down_diag, best)


def solve():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    # x - y 인덱스를 - (n-1) ~ (n-1) 로 맞추기 위해 dict 초기화
    used_down_diag = {}
    for diff in range(-n + 1, n):
        used_down_diag[diff] = 0

    best_result = [0]  # 리스트로 감싸서 참조로 사용
    backtrack(0, 0, n, board, used_down_diag, best_result)
    print(best_result[0])


solve()
