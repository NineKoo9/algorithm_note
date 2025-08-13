package 토마토;

import java.io.*;
import java.util.*;

public class Main {
    static int height;
    static int width;
    
    static int[][] tomatoBoard;
    static List<Point> ripeTomatoes;
    static int unRipeTomatoCount = 0;

    static int[] dr = new int[] {0, 0, 1, -1};
    static int[] dc = new int[] {1, -1, 0, 0};

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        width = Integer.parseInt(st.nextToken());
        height = Integer.parseInt(st.nextToken());

        tomatoBoard = new int[height][width];
        ripeTomatoes = new ArrayList<>();

        for (int i = 0; i < height; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < width; j++) {
                tomatoBoard[i][j] = Integer.parseInt(st.nextToken());
                if (tomatoBoard[i][j] == 1) {
                    ripeTomatoes.add(new Point(i, j));
                }
                if (tomatoBoard[i][j] == 0) {
                    unRipeTomatoCount++;
                }
            }
        }

        int ans = 0;

        Queue<Point> q = new LinkedList<>();
        for (Point point : ripeTomatoes) {
            int r = point.r;
            int c = point.c;
            q.offer(new Point(r, c, 0));
        }

        while (!q.isEmpty()) {
            Point point = q.poll();
            int curR = point.r;
            int curC = point.c;
            int curDist = point.dist;

            ans = Math.max(ans, curDist);

            for (int i = 0; i < 4; i++) {
                int nxtR = curR + dr[i];
                int nxtC = curC + dc[i];
                if (nxtR < 0 || nxtR >= height || nxtC < 0 || nxtC >= width) {
                    continue;
                }
                if (tomatoBoard[nxtR][nxtC] == 0) {
                    tomatoBoard[nxtR][nxtC] = 1;
                    unRipeTomatoCount--;
                    q.offer(new Point(nxtR, nxtC, curDist + 1));
                }
            }
        }

        System.out.println(unRipeTomatoCount == 0 ? ans : -1);


    }

    static class Point {
        int r;
        int c;
        int dist;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public Point(int r, int c, int dist) {
            this.r = r;
            this.c = c;
            this.dist = dist;
        }

        @Override
        public String toString() {
            return "(r=" + r + ", " + "c=" + c + ")";
        }
    }
    
}
