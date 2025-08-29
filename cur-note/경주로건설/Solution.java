import java.util.*;

class Solution {
    static int[] dx = new int[] {1, 0, -1, 0};
    static int[] dy = new int[] {0, 1, 0, -1};
    static int N;
    static int[][] board;
    static int[][][] dp;
    static boolean[][] visited;
    static int INF = 100000000;
    
    public int dfs(int y, int x, int prevDirect) {
        if (y == N - 1 && x == N - 1) {
            return 0;
        }
        
        if (dp[y][x][prevDirect] != INF) {
            return dp[y][x][prevDirect];
        }
        
        for (int nxtDirect = 0; nxtDirect < 4; nxtDirect++) {
            int ny = y + dy[nxtDirect];
            int nx = x + dx[nxtDirect];
            // board을 벗어나거나 벽 or 지나온 칸이라면 탐색하지 않는다.
            if (ny < 0 || ny >= N || nx < 0 || nx >= N || board[ny][nx] == 1 || visited[ny][nx]) {
                continue;
            } 
            // 이제부터 탐색을 하는데, 비용도 계산해야하고,,,
            visited[ny][nx] = true;
            int cost = dfs(ny, nx, nxtDirect) + ((prevDirect != nxtDirect) ? 600 : 100);
            dp[y][x][prevDirect] = Math.min(dp[y][x][prevDirect], cost);
            visited[ny][nx] = false;
        }
        return dp[y][x][prevDirect];
    }
    
    public int solution(int[][] input) {
        // 경주로를 건설하는데 필요한 최소 비용을 계산해야한다.
        // 모든 경우를 다 탐색해야할 필요가 있을듯한데 이러면 중복이 발생한다.
        // 그렇다면.. 역시 백트래킹과 메모이제이션인가? 특정 지점에서 그 비용이 다를 수 있다.
        // 그렇다면 겹치는 부분 문제가 존재하나? 진입 지점에 따라 다르지만 진입 지점이 같다면? 특정 인자가 진입지점이 될 수 있다.
        // 일단 완전 탐색을 해볼까? 이 모든 길을 dfs로 다 따진다는게 말도 안된다는 것을 처음 생각했어야지
        // 맞아 말이 안되니까 dp를 사용해야겠다고 생각했어.
        // 근데 확실히 dfs로 하니까 불필요하게 최단경로가 아닌 경우도 탐색을 하게되네... 흠
        // 그렇다면 bfs로 dp를 수행해보자.
        board = input;
        N = board.length;
        // dp초기화
        dp = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    dp[i][j][k] = INF;
                }
            }
        }

        // return Math.min(dfs(0, 0, 0), dfs(0, 0, 1));
        Queue<State> q = new LinkedList<>();
        q.add(new State(0, 0, 0, 0));
        q.add(new State(0, 0, 0, 1));
        dp[0][0][0] = 0;
        dp[0][0][1] = 0;

        while (!q.isEmpty()) {
            State curState = q.poll();
            int y = curState.y;
            int x = curState.x;
            int prevDirect = curState.direct;
            int cost = curState.cost;

            // 이미 방문했던 지점이라면?
            // 흠... bfs로 간다했을때 이 부분이 최단거리라고 보장할 수 있나? 그렇다면 이 부분은 다익스트라로 가야할듯?
            // 여기서 메모이제이션을 사용하면 후에 같은 경우라도 더 비용이 작은 경우 갱신을 할 수 없게 된다.
            // if (dp[y][x][prevDirect] != INF) {
            //     return dp[y][x][prevDirect];
            // }

            for (int nxtDirect = 0; nxtDirect < 4; nxtDirect++) {
                int ny = y + dy[nxtDirect];
                int nx = x + dx[nxtDirect];
                // board을 벗어나거나 벽은 탐색하지 않는다.
                if (ny < 0 || ny >= N || nx < 0 || nx >= N || board[ny][nx] == 1) {
                    continue;
                } 

                // 이제부터 탐색을 하는데, 비용도 계산해야하고,,,
                int nxtCost = cost + ((prevDirect != nxtDirect) ? 600 : 100);
                if (dp[ny][nx][nxtDirect] > nxtCost) {
                    dp[ny][nx][nxtDirect] = nxtCost;
                    q.add(new State(ny, nx, dp[ny][nx][nxtDirect], nxtDirect));
                }
            }


        }
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < 4; i++) {
            ans = Math.min(ans, dp[N - 1][N - 1][i]);
        }

        return ans;
        
    }
    
    static class State {
        int y;
        int x;
        int cost;
        int direct;
        
        public State(int y, int x, int cost, int direct) {
            this.y = y;
            this.x = x;
            this.cost = cost;
            this.direct = direct;
        }
    }
}