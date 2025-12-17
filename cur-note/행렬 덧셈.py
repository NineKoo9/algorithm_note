def solution():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(N)]
    
    # 이제부터 행렬의 덧셈을 수행한다. 시간복잡도는 N * M인데 이것을 최적화할 수 있을까?
    C = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            C[i][j] = A[i][j] + B[i][j]
    for row in C:
        print(*row)

solution()