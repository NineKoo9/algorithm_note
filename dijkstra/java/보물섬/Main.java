package 보물섬;

import java.util.*;
import java.io.*;

public class Main {
    static int height;
    static int width;
    static char[][] board;
    static boolean[][] visited;

    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    static int ans = 0;

    public static void bfs(int u, int v) {
        visited = new boolean[height][width];
        visited[u][v] = true;
        
        Queue<Pair> q = new LinkedList<>();
        q.offer(new Pair(u, v, 0));

        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int r = pair.u;
            int c = pair.v;
            int time = pair.time;
            if (ans < time) {
                ans = time;
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (nr < 0 || nr >= height || nc < 0 || nc >= width) {
                    continue;
                }
                if (visited[nr][nc] || board[nr][nc] == 'W') {
                    continue;
                }
                visited[nr][nc] = true;
                q.offer(new Pair(nr, nc, time + 1));
            }
        }
    }
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        height = Integer.parseInt(st.nextToken());
        width = Integer.parseInt(st.nextToken());

        board = new char[height][width];
        for (int i = 0; i < height; i++) {
            String line = br.readLine();
            for (int j = 0; j < width; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (board[i][j] == 'W') {
                    continue;
                }
                bfs(i, j);
            }
        }

        System.out.println(ans);
    }

    public static class Pair {
        int u;
        int v;
        int time;

        public Pair(int u, int v, int time) {
            this.u = u;
            this.v = v;
            this.time = time;
        }

        @Override
        public String toString() {
            return "(u=" + u + ", " + "v=" + v + "time=" + time + ")";
        }
    }
}