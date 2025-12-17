def solution():
    N, M, K = map(int, input().split()) # n*m 에서 잘라서 k크기의 체스판을 만들려고한다.
    board = [list(input()) for _ in range(N)]
    mask1 = [[0 if (i + j) % 2 == 0 else 1 for i in range(M)] for j in range(N)] # 일단 여기서.. 더했을때 짝수 홀수에 따라서 색깔을 구분하는 것도 쉽지는 않았을 것이다.
    mask2 = [[0 if (i + j) % 2 != 0 else 1 for i in range(M)] for j in range(N)] # 1이면 W라 생각하자
    # 여기서 기존의 board을 mask1에 맞게 설정한다면... 몇개를 바꿔야할까? 바꿔야할 부분을 어떻게 체크를 하지?
    # mask1을 board에 맞게 설정해나가보자. 중요한 것은 board에서 새롭게 색칠해야하는 부분을 체크를 한다는 것이다.
    for i in range(N):
        for j in range(M):
            mask1[i][j] = 0 if (board[i][j] == 'B' and mask1[i][j] == 0) or (board[i][j] == 'W' and mask1[i][j] == 1) else 1
            mask2[i][j] = 0 if (board[i][j] == 'B' and mask2[i][j] == 0) or (board[i][j] == 'W' and mask2[i][j] == 1) else 1
    # 이제부터 k개 만큼 잘라낼 것인데... 그 안에 1 이 몇개가 있는지를 누적합을 이용할 것이다.
    # 1이 몇개인지 하나하나 세는 것은 너무 복잡하며... 크기가 k 인 경우를 계속 옮겨줘야해서 어마어마한 연산이 소모된다.
    mask1_sum_table = [[0] * M for _ in range(N)]
    mask2_sum_table = [[0] * M for _ in range(N)]
    # 먼저 가로 합
    for i in range(N):
        for j in range(M):
            mask1_sum_table[i][j] = (mask1_sum_table[i][j - 1] if j - 1 >= 0 else 0) + mask1[i][j]
            mask2_sum_table[i][j] = (mask2_sum_table[i][j - 1] if j - 1 >= 0 else 0) + mask2[i][j]
    # 세로 합
    for i in range(N):
        for j in range(M):
            mask1_sum_table[i][j] = (mask1_sum_table[i - 1][j] if i - 1 >= 0 else 0) + mask1_sum_table[i][j]
            mask2_sum_table[i][j] = (mask2_sum_table[i - 1][j] if i - 1 >= 0 else 0) + mask2_sum_table[i][j]
    min_value = int(1e9)
    # k * k 의 구간의 누적합을 구했을때 제일 작은 것을 찾아야 한다...
    for i in reversed(range(N)):
        for j in reversed(range(M)):
            if i - K >= -1 and j - K >= -1:
                min_value = min(min_value, \
                                mask1_sum_table[i][j] - (mask1_sum_table[i - K][j] if i - K >= 0 else 0) - (mask1_sum_table[i][j - K] if j - K >= 0 else 0) + (mask1_sum_table[i - K][j - K] if i - K >= 0 and j - K >= 0 else 0), \
                                mask2_sum_table[i][j] - (mask2_sum_table[i - K][j] if i - K >= 0 else 0) - (mask2_sum_table[i][j - K] if j - K >= 0 else 0) + (mask2_sum_table[i - K][j - K] if i - K >= 0 and j - K >= 0 else 0))
    print(min_value)
    pass



def solution2():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    M = int(data[1])
    K = int(data[2])
    board = [data[i + 3] for i in range(N)]

    # 체스판 패턴에 따른 마스크 생성
    def create_masks(N, M, board):
        mask1, mask2 = [], []
        for i in range(N):
            row1, row2 = [], []
            for j in range(M):
                expected = 'B' if (i + j) % 2 == 0 else 'W'
                row1.append(0 if board[i][j] == expected else 1)
                row2.append(0 if board[i][j] != expected else 1)
            mask1.append(row1)
            mask2.append(row2)
        return mask1, mask2

    # 누적합 계산
    def compute_cumulative_sums(mask, N, M):
        sum_table = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                sum_table[i][j] = mask[i][j] + (sum_table[i][j - 1] if j > 0 else 0)
                if i > 0:
                    sum_table[i][j] += sum_table[i - 1][j]
        return sum_table

    # 최소 변경 수 계산
    def min_changes(sum_table, N, M, K):
        min_value = float('inf')
        for i in range(K - 1, N):
            for j in range(K - 1, M):
                top = sum_table[i - K][j] if i >= K else 0
                left = sum_table[i][j - K] if j >= K else 0
                corner = sum_table[i - K][j - K] if i >= K and j >= K else 0
                total = sum_table[i][j] - top - left + corner
                min_value = min(min_value, total)
        return min_value

    mask1, mask2 = create_masks(N, M, board)
    mask1_sum_table = compute_cumulative_sums(mask1, N, M)
    mask2_sum_table = compute_cumulative_sums(mask2, N, M)

    result1 = min_changes(mask1_sum_table, N, M, K)
    result2 = min_changes(mask2_sum_table, N, M, K)
    print(min(result1, result2))

def solution3():
    N, M, K = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    board_a = [["B" if (i + j) % 2 == 0 else "W" for j in range(M)] for i in range(N)]
    board_b = [["W" if (i + j) % 2 == 0 else "B" for j in range(M)] for i in range(N)]
    a_diff = [[0 for _ in range(M)] for _ in range(N)]
    b_diff = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != board_a[i][j]:
                a_diff[i][j] = 1
            if board[i][j] != board_b[i][j]:
                b_diff[i][j] = 1
    sum_table_a = [[0 for _ in range(M)] for _ in range(N)]
    sum_table_b = [[0 for _ in range(M)] for _ in range(N)]
    # sum_table을 어떻게 만들어갈것이냐?
    # 먼저 가로합
    for i in range(N):
        for j in range(M):
            sum_table_a[i][j] += a_diff[i][j] + (sum_table_a[i][j - 1] if j - 1 >= 0 else 0)
            sum_table_b[i][j] += b_diff[i][j] + (sum_table_b[i][j - 1] if j - 1 >= 0 else 0)
    # 이제 세로합
    for i in range(1, N):
        for j in range(M):
            sum_table_a[i][j] += sum_table_a[i - 1][j]
            sum_table_b[i][j] += sum_table_b[i - 1][j]
    # 이제 최소 결과를 구하자
    min_result = int(1e8)
    for i in range(K - 1, N):
        for j in range(K - 1, M):
            a_result = sum_table_a[i][j] - (sum_table_a[i][j - K] if j - K >= 0 else 0) \
                       - (sum_table_a[i - K][j] if i - K >= 0 else 0) \
                       + (sum_table_a[i - K][j - K] if i - K >= 0 and j - K >= 0 else 0)
            b_result = sum_table_b[i][j] - (sum_table_b[i][j - K] if j - K >= 0 else 0) \
                       - (sum_table_b[i - K][j] if i - K >= 0 else 0) \
                       + (sum_table_b[i - K][j - K] if i - K >= 0 and j - K >= 0 else 0)
            min_result = min(min_result, a_result, b_result)

    print(min_result)

def solution4():
    N, M, K = map(int, input().split())
    board = [input() for _ in range(N)]

    white_board = [["W" if (i + j) % 2 == 0 else "B" for j in range(M) ] for i in range(N)]
    black_board = [["B" if (i + j) % 2 == 0 else "W" for j in range(M)] for i in range(N)]

    white_board_diff = [[0 for _ in range(M)] for _ in range(N)]
    black_board_diff = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] != white_board[i][j]:
                white_board_diff[i][j] = 1
            if board[i][j] != black_board[i][j]:
                black_board_diff[i][j] = 1

    white_board_diff_sum = [[0] * M for _ in range(N)]
    black_board_diff_sum = [[0] * M for _ in range(N)]

    # 먼저 가로 합을 모두 구한다.
    for i in range(N):
        for j in range(M):
            white_board_diff_sum[i][j] = (white_board_diff_sum[i][j - 1] if j - 1 >= 0 else 0) + white_board_diff[i][j]
            black_board_diff_sum[i][j] = (black_board_diff_sum[i][j - 1] if j - 1 >= 0 else 0) + black_board_diff[i][j]
    # 이제 새로 합을 구한다.
    for j in range(M):
        for i in range(N):
            white_board_diff_sum[i][j] = (white_board_diff_sum[i - 1][j] if i - 1 >= 0 else 0) + white_board_diff_sum[i][j]
            black_board_diff_sum[i][j] = (black_board_diff_sum[i - 1][j] if i - 1 >= 0 else 0) + black_board_diff_sum[i][j]

    min_result = int(1e8)
    for i in range(K - 1, N):
        for j in range(K - 1, M):
            a_result = white_board_diff_sum[i][j] - (white_board_diff_sum[i][j - K] if j - K >= 0 else 0) \
                       - (white_board_diff_sum[i - K][j] if i - K >= 0 else 0) \
                       + (white_board_diff_sum[i - K][j - K] if i - K >= 0 and j - K >= 0 else 0)
            b_result = black_board_diff_sum[i][j] - (black_board_diff_sum[i][j - K] if j - K >= 0 else 0) \
                       - (black_board_diff_sum[i - K][j] if i - K >= 0 else 0) \
                       + (black_board_diff_sum[i - K][j - K] if i - K >= 0 and j - K >= 0 else 0)
            min_result = min(min_result, a_result, b_result)
    print(min_result)


solution4()