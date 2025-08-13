package 촌수계산;

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int from;
    static int to;
    static int M;
    static List<List<Integer>> graph;

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        from = Integer.parseInt(st.nextToken());
        to = Integer.parseInt(st.nextToken());

        M = Integer.parseInt(br.readLine());

        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int u = Integer.parseInt(st.nextToken());
            graph.get(v).add(u);
            graph.get(u).add(v);
        }

        System.out.println("graph: " + graph);

        // 여기서부터 bfs를 시작하자.
        int ans = -1;
        boolean[] visited = new boolean[N + 1];
        visited[from] = true;

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{from, 0});

        while (!q.isEmpty()) {
            int[] element = q.poll();
            int cur = element[0];
            int dist = element[1];

            if (cur == to) {
                ans = dist;
                break;
            }

            for (int nextNode : graph.get(cur)) {
                if (visited[nextNode]) continue;
                visited[nextNode] = true;
                q.offer(new int[]{nextNode, dist + 1});
            }
        }

        System.out.println(ans);
    }
}
