package 빵집;

import java.io.*;
import java.util.*;

public class Main {
    static int R;
    static int C;
    static char[][] board;
    static boolean[][] visited;
    static int[] dr = new int[] {-1, 0, 1};
    static int[] dc = new int[] {1, 1, 1};
    static int pipeCnt = 0;

    public static boolean dfs(int r, int c) {
        if (c == C - 1) {
            return true;
        }

        for (int i = 0; i < 3; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
            if (visited[nr][nc]) continue;
            if (board[nr][nc] == 'x') continue;
            visited[nr][nc] = true;
            boolean result = dfs(nr, nc);
            if (result) return true;
        }

        return false;
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        // 지도 초기화
        board = new char[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        // visited
        visited = new boolean[R][C];

        // 각 행별로 dfs 수행
        for (int start = 0; start < R; start++) {
            if (board[start][0] == 'x') continue;
            visited[start][0] = true;
            pipeCnt = dfs(start, 0) ? pipeCnt + 1 : pipeCnt;
        }

        System.out.println(pipeCnt);
    }
}
