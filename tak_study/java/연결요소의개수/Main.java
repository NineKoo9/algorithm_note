package 연결요소의개수;

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static List<List<Integer>> graph = new ArrayList<>();
    static boolean[] visited;
    static int ans;

    public static void dfs(int start) {
        visited[start] = true;
        for (int nextNode : graph.get(start)) {
            if (visited[nextNode]) continue;
            visited[nextNode] = true;
            dfs(nextNode);
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()) - 1;
            int v = Integer.parseInt(st.nextToken()) - 1;
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        visited = new boolean[N];
        Arrays.fill(visited, false);
        for (int curNode = 0; curNode < N; curNode++) {
            if (visited[curNode]) continue;
            dfs(curNode);
            ans++;
        }
        System.out.println(ans);
    }
}
