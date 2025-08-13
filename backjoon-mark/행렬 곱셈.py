def solution():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    M, K = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(M)]
    
    result = [[0] * K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            r = 0
            for m_i in range(M):
                r += A[i][m_i] * B[m_i][j]
            result[i][j] = r
    for row in result:
        print(*row)
            

solution()