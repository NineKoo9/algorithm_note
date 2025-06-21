package 가장작은직사각형;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        
        List<Integer> xs = new ArrayList<>();
        List<Integer> ys = new ArrayList<>();
        Point[] points = new Point[N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int X = Integer.parseInt(st.nextToken());
            int Y = Integer.parseInt(st.nextToken());
            xs.add(X);
            ys.add(Y);
            Point p = new Point(X, Y);
            points[i] = p;
        }

        xs = xs.stream().distinct().sorted().collect(Collectors.toList());
        ys = ys.stream().distinct().sorted().collect(Collectors.toList());

        int xsSize = xs.size();
        int ysSize = ys.size();

        int[][] grid = new int[xsSize][ysSize];

        for (Point p : points) {
            int xIdx = Collections.binarySearch(xs, p.x);
            int yIdx = Collections.binarySearch(ys, p.y);
            grid[xIdx][yIdx] = 1;
        }

        // 자 이제 압축된 좌표를 기준으로 점이 몇개 있는지 구하자.
        // prefix[i + 1][j + 1]은 (0, 0) ~ (i, j) 까지의 갯수
        int[][] prefixCount = new int[xsSize + 1][ysSize + 1];
        for (int i = 1; i <= xsSize; i++) {
            for (int j = 1; j <= ysSize; j++) {
                prefixCount[i][j] = grid[i - 1][j - 1] + prefixCount[i - 1][j] + prefixCount[i][j - 1] - prefixCount[i - 1][j - 1];
            }
        }

        // 이제 범위를 좁혀가며 구하면 된다.
        int ans = Integer.MAX_VALUE;
        for (int lx = 0; lx < xsSize; lx++) {
            for (int rx = lx; rx < xsSize; rx++) {
                // 이제 y좌표의 범위를 슬라이딩 윈도우로 따져본다.
                for (int dy = 0, uy = 0; dy < ysSize; dy++) {

                    if (dy > uy) {
                        uy = dy;
                    }

                    while (uy < ysSize && prefixCount[rx + 1][uy + 1] - prefixCount[rx + 1][dy] - prefixCount[lx][uy + 1] + prefixCount[lx][dy] < N/2) {
                        uy++;
                    }

                    if (uy >= ysSize) {
                        break;
                    }

                    int width = xs.get(rx) - xs.get(lx) + 2;
                    int height = ys.get(uy) - ys.get(dy) + 2;
                    ans = Math.min(ans, width * height);
                }
            }
        }

        System.out.println(ans);
    }
    
    static class Point {
        int x;
        int y;

        public Point (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
