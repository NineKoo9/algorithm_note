package 단지번호붙이기;

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[][] board;
    static boolean[][] visited;

    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    public static int bfs(int v, int u) {
        int cnt = 1;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{v, u});
        visited[v][u] = true;

        while (!q.isEmpty()) {
            int[] curNode = q.poll();
            int r = curNode[0];
            int c = curNode[1];

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                if (visited[nr][nc] || board[nr][nc] == 0) continue;
                visited[nr][nc] = true;
                q.offer(new int[]{nr, nc});
                cnt++;
            }
        }
        return cnt;
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        board = new int[N][N];
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = line.charAt(j) - '0';
            }
        }

        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j] || board[i][j] == 0) continue;
                ans.add(bfs(i, j));
            }
        }

        Collections.sort(ans);
        System.out.println(ans.size());
        for (int c : ans) {
            System.out.println(c);
        }
    }
}
