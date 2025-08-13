package 암벽등반;

import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int T;

    static Set<Point> nodeSet;
    static Map<Point, Boolean> visited;

    static int[] dx = new int[] {-2, -1, 0, 1, 2, -2, -1, 0, 1, 2, -2, -1, 1, 2, -2, -1, 0, 1, 2, -2, -1, 0, 1, 2};
    static int[] dy = new int[] {2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2};



    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        nodeSet = new HashSet<>();
        visited = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            Point point = new Point(x, y);

            nodeSet.add(new Point(x, y));
            visited.put(point, false);
        }

        Point start = new Point(0, 0);

        Queue<Pair> q = new LinkedList<>();
        q.offer(new Pair(start, 0));

        int ans = -1;
        while (!q.isEmpty()) {
            Pair pair = q.poll();
            Point curPoint = pair.point;
            int curDist = pair.dist;

            if (curPoint.y == T) {
                ans = curDist;
                break;
            }

            for (int i = 0; i < 24; i++) {
                int nx = curPoint.x + dx[i];
                int ny = curPoint.y + dy[i];
                if (nx < 0 || nx > 1000001 || ny < 0 || ny > T) {
                    continue;
                }
                Point nextPoint = new Point(nx, ny);
                if (!nodeSet.contains(nextPoint)) {
                    continue;
                }

                if (visited.get(nextPoint)) {
                    continue;
                }

                visited.put(nextPoint, true);
                q.offer(new Pair(nextPoint, curDist + 1));
            }
        }

        System.out.println(ans);
    }

    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "(" + "x=" + x + ", " + "y=" + y + ")"; 
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (!(o instanceof Point)) {
                return false;
            }
            Point point = (Point) o;
            return this.x == point.x && this.y == point.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    static class Pair {
        Point point;
        int dist;

        public Pair(Point point, int dist) {
            this.point = point;
            this.dist = dist;
        }

        @Override
        public String toString() {
            return "(" + "point=" + point + ", " + "dist=" + dist + ")"; 
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (!(o instanceof Pair)) {
                return false;
            }
            Pair other = (Pair) o;
            return this.point == other.point && this.dist == other.dist;
        }

        @Override
        public int hashCode() {
            return Objects.hash(point, dist);
        }
    }
    
}
