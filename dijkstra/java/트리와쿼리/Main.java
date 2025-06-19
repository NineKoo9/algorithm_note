package 트리와쿼리;

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int R;
    static int Q;
    static List<List<Integer>>tree;
    static int[] subTreeCount;

    public static int dfs(int node, int prev) {
        int subCount = 1;

        for (int nextNode : tree.get(node)) {
            if (nextNode == prev) {
                continue;
            }
            subCount += dfs(nextNode, node);
        }
        subTreeCount[node] = subCount;
        return subCount;
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        tree = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            tree.add(new ArrayList<>());
        }
        subTreeCount = new int[N + 1];

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int U = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());
            tree.get(U).add(V);
            tree.get(V).add(U);
        }

        dfs(R, R);

        for (int i = 0; i < Q; i++) {
            int U = Integer.parseInt(br.readLine());
            System.out.println(subTreeCount[U]);
        }
    }
}
