package 알파벳;

import java.io.*;
import java.util.*;

public class Main {
    static int R;
    static int C;
    static char[][] board;
    static int maxCnt = 0;

    static int[] dr = new int[]{1, -1, 0, 0};
    static int[] dc = new int[]{0, 0, 1, -1};

    static Map<Character, Boolean> visited;

    public static void dfs(int r, int c, int cnt) {
        visited.put(board[r][c], true);
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
            if (visited.get(board[nr][nc])) continue;
            dfs(nr, nc, cnt + 1);
        }
        visited.put(board[r][c], false);

        maxCnt = Math.max(maxCnt, cnt);
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        
        board = new char[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        visited = new HashMap<>();
        for (char c = 'A'; c <= 'Z'; c++) {
            visited.put(c, false);
        }

        dfs(0, 0, 1);
        System.out.println(maxCnt);
    }
}
