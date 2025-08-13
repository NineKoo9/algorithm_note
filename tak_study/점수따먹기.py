import sys
input = sys.stdin.readline

# 이 코드는 시간이 너무 많이 걸린다.
def solution():
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 이 누적 prefix_sum[i+1][j+1]은 (0, 0) ~ (i, j) 이다.
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i][j - 1]
    for j in range(1, M + 1):
        for i in range(1, N + 1):
            prefix_sum[i][j] += prefix_sum[i - 1][j]
            
    # 여기서부터 최대합의 부분행렬을 구해야한다.
    # 단순하게 생각하면 완전탐색으로 볼 수 있다.
    max_value = -int(1e9)
    for i in range(N):
        for j in range(M):
            for u in range(i, N):
                for v in range(j, M):
                    sub_matrix_sum = prefix_sum[u + 1][v + 1] - prefix_sum[u + 1][j] - prefix_sum[i][v + 1] + prefix_sum[i][j]
                    max_value = max(max_value, sub_matrix_sum)
    print(max_value)


# 부분 행렬을 어떻게 탐색하느냐에 따라서 시간복잡도 차이가 어마어마하다.
# 윗줄(top)–아랫줄(bot)”을 고정 ⇒ 해당 두 행 사이를 1 차원 배열로 압축한 뒤 Kadane(1 차원 최대 부분합)
# 차원을 하나 줄임으로써 시간복잡도 차이가 어마어마하게 변할 수 있다.
def solution2():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    prefix = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            prefix[i][j] = prefix[i][j - 1] + A[i - 1][j - 1]
        for j in range(1, M + 1):
            prefix[i][j] += prefix[i - 1][j]

    best = -int(1e9)
    for top in range(N):
        for bot in range(top, N):
            colSum = [0] * M
            for j in range(M):
                colSum[j] = prefix[bot + 1][j + 1] - prefix[top][j + 1] - prefix[bot + 1][j] + prefix[top][j]

            cur = colSum[0] 
            best = max(best, cur) # 이것을 넣지 않으면 첫번째 열의 비교가 생략되기에 추가한다.
            for x in colSum[1:]:
                cur = max(x, cur + x) # j의 기존 값부터 이어오거나 아니면 다시 시작하거나 그 차이네...
                best = max(best, cur)

    print(best)

solution2()