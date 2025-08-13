package 트리의부모찾기;

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static List<List<Integer>> graph;
    static int[] parentTable;

    public static void dfs(int node, int prev) {
        parentTable[node] = prev;
        
        for (int nextNode : graph.get(node)) {
            if (nextNode == prev) {
                continue;
            }
            dfs(nextNode, node);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            graph.get(node1).add(node2);
            graph.get(node2).add(node1);
        }

        // 그래프를 초기화했으니까 루트 1번부터 탐색을 이어나가자.
        parentTable = new int[N + 1];

        dfs(1, 1);
        for (int i = 2; i < N + 1; i++) {
            System.out.println(parentTable[i]);
        }

    }
    
}
