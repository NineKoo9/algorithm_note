package 넷이놀기;

import java.util.*;
import java.io.*;

// 이거 그냥 똑같은 논리로 파이썬으로 진행함..
public class Main {
    static int N;
    static int A;
    static int B;
    static int[][] points;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        points = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            points[i][0] = Integer.parseInt(st.nextToken());
            points[i][1] = Integer.parseInt(st.nextToken());
        }

        Set<Point> pointSet = new HashSet<>();
        for (int i = 0; i < N; i++) {
            pointSet.add(new Point(points[i][0], points[i][1]));
        }

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            Point point1 = new Point(points[i][0], points[i][1]);
            Point point2 = new Point(points[i][0] + A, points[i][1]);
            Point point3 = new Point(points[i][0], points[i][1] + B);
            Point point4 = new Point(points[i][0] + A, points[i][1] + B);
            if (pointSet.contains(point1) && pointSet.contains(point2) && pointSet.contains(point3) && pointSet.contains(point4)) {
                cnt++;
            }
        }

        System.out.println(cnt);
    }

    public static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Point other = (Point) obj;
            return x == other.x && y == other.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
}
