package 바이러스;

import java.util.*;
import java.io.*;

public class Main {
    static int computerNum;
    static int networkNum;
    static List<List<Integer>> graph = new ArrayList<>();
    static int[] visited;
    static int ans;

    public static void dfs(int start) {
        
        for (int nextNode : graph.get(start)) {
            if (visited[nextNode] == 1) continue;
            visited[nextNode] = 1;
            ans++;
            dfs(nextNode);
        }
        return;
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        computerNum = Integer.parseInt(br.readLine());
        networkNum = Integer.parseInt(br.readLine());

        // 그래프 초기화
        for (int i = 0; i < computerNum; i++) {
            graph.add(new ArrayList<>());
        }

        // 간선 초기화
        for (int i = 0; i < networkNum; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken()) - 1;
            int u = Integer.parseInt(st.nextToken()) - 1;
            graph.get(v).add(u);
            graph.get(u).add(v);
        }
        
        visited = new int[computerNum];
        Arrays.fill(visited, 0);
        
        visited[0] = 1;
        dfs(0);
        System.out.println(ans);
    }
}
