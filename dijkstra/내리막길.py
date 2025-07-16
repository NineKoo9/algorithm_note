import sys

sys.setrecursionlimit(100000)

# 내리막길 탑다운으로 풀었다.
def solution():
    def recur(r, c):
        # 도착한다면? 경로가 0
        if (r, c) == (M - 1, N - 1):
            return 1

        if dp[r][c] != -1:
            return dp[r][c]

        count = 0
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            # 오르막길이거나 같다면 갈 수 없다. 어짜피 지나온 길도 오르막길이니 가지못할 것이다.
            if not(0 <= n_r < M and 0 <= n_c < N) or board[r][c] <= board[n_r][n_c]:
                continue
            count += recur(n_r, n_c)
        dp[r][c] = count
        return count

    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(M)]
    dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]
    dp = [[-1] * N for _ in range(M)]
    print(recur(0, 0))

def solution2():
    def dfs(r, c):
        if (r, c) == (M - 1, N - 1):
            return 1
        
        if dp[r][c] != -1:
            return dp[r][c]
        
        count = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 보드 범위를 벗어난 경우
            if not (0 <= nr < M and 0 <= nc < N):
                continue
            # 같거나 오르막길인 경우
            if board[r][c] <= board[nr][nc]:
                continue
            count += dfs(nr, nc)
        dp[r][c] = count
        return count
    
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(M)] 
    
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    dp = [[-1] * N for _ in range(M)]
    
    print(dfs(0, 0))

solution2()