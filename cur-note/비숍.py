import sys

input = sys.stdin.readline
max_bishop_count = 0

# 이 풀이는 최악의 경우 시간복잡도가 N^(2N)이 된다.. 각 대각선에서 최악의 경우 N이고 그때마다 check에서 2N-2개까지 탐색할 수 있으니까..
def solution():
    global max_bishop_count

    def check(u, v, cross_idx):  # 우하향에 현재 값이 있는지 체크해줘야한다.
        # 좌표 u, v에
        for prev_cross_idx in range(cross_idx):
            # 여기서 비숍의 위치를 가져와야지
            prev_bishop = bishop_dp[prev_cross_idx]
            # -1인경우는 비숍이 없는 경우고.. 그게 아니라면 비숍이 있으니 우하향으로 체크를 해봐야한다.
            if prev_bishop != -1 and abs(prev_bishop[0] - u) == abs(prev_bishop[1] - v):
                return False
        return True

    def dfs(cross_idx, cur_bishop_count):
        global max_bishop_count

        if cross_idx == 2 * N - 1:
            max_bishop_count = max(max_bishop_count, cur_bishop_count)
            return

        if cross_board[cross_idx]:
            for y, x in cross_board[cross_idx]: # 아 지금보니까... 5에 놓을 수 있는 것이 없는 경우가 있다.
                bishop_dp[cross_idx] = (y, x)  # 이것을 놓을 수 있냐 없냐를 매우 빠르게 체크할 수없을까?
                next_bishop_count = cur_bishop_count + 1
                if not check(y, x, cross_idx):  # 놓을 수 없다면 취소한다.. 그
                    bishop_dp[cross_idx] = -1
                    next_bishop_count -= 1
                dfs(cross_idx + 1, next_bishop_count) # 탐색을 하고...

        else:  # 만약 놓을 수 있는 대각선 좌표가 없다면?
            # 없다면... 그냥 탐색해나간다.
            dfs(cross_idx + 1, cur_bishop_count)

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]  # 1이면 비숍가능 0이면 비숍불가

    cross_board = [[] for _ in range(2 * N - 1)]  # 여기에는 K번째 우상향 대각선에서 비숍을 놓을 수 있는 위치다.

    bishop_dp = [-1 for _ in range(2 * N - 1)]  # 여기에는 k번째 우상향 대각선에서 비숍이 있는 좌표를 뜻한다.

    # 사선 몇번에는 어떤 좌표들이 있는지 체크해야겠다.
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cross_board[i + j].append((i, j))
    dfs(0, 0)
    print(max_bishop_count)



def solution2():
    global max_bishop_count

    def check(u, v):  # 우하향에 현재 값이 있는지 체크해줘야한다.
        # u, v이면... 우하향 몇번째이지? 그냥 u - v을 우하향 인덱스로 설정하자.
        if right_downward[u - v] == 1:  # 현재 여기에 값이 존재한다면 안된다...
            return False
        return True

    def dfs(cross_idx, cur_bishop_count):
        global max_bishop_count

        if cross_idx == 2 * N - 1:
            max_bishop_count = max(max_bishop_count, cur_bishop_count)
            return

        flag = False
        for y, x in cross_board[cross_idx]: # 아 지금보니까... 5에 놓을 수 있는 것이 없는 경우가 있다.
            if check(y, x):
                flag = True
                bishop_dp[cross_idx] = (y, x)  # 이것을 놓을 수 있냐 없냐를 매우 빠르게 체크할 수없을까?
                right_downward[y - x] = 1
                dfs(cross_idx + 1, cur_bishop_count + 1) # 탐색을 하고...
                bishop_dp[cross_idx] = -1
                right_downward[y - x] = -1
        # 이것은... 이번라인에서 아무것도 놓을 곳이 없거나?
        if not flag:  # flag가 없다면... 이미 위에서 비숍을 놓은 경우를 모두 탐색했는데 비숍을 안놓고 건너뛰어서 다시 탐색한다.
            # 즉 비숍을 놓은 적이 있다면.. 추가로 탐색할 필요는 없다.
            dfs(cross_idx + 1, cur_bishop_count)

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]  # 1이면 비숍가능 0이면 비숍불가

    cross_board = [[] for _ in range(2 * N - 1)]  # 여기에는 K번째 우상향 대각선에서 비숍을 놓을 수 있는 위치다.

    bishop_dp = [-1 for _ in range(2 * N - 1)]  # 여기에는 k번째 우상향 대각선에서 비숍이 있는 좌표를 뜻한다.
    right_downward = {i: -1 for i in range(-N - 1, N + 1)}

    # 사선 몇번에는 어떤 좌표들이 있는지 체크해야겠다.
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cross_board[i + j].append((i, j))
    dfs(0, 0)
    print(max_bishop_count)

solution2()