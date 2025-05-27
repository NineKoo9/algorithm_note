package 숫자고르기;

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] arr;
    static boolean[] visited;
    static boolean[] isCycle;
    static Set<Integer> path;

    public static void dfs(int node) {
        path.add(node);

        int nextNode = arr[node];
        if (!visited[nextNode]) {
            if (!path.contains(nextNode)) {
                dfs(nextNode);
            } else {  // 사이클을 이룬다면? 사이클을 탐색하며 true로 바꿔준다.
                isCycle[nextNode] = true;
                for (int i = arr[nextNode]; i != nextNode; i = arr[i]) {
                    isCycle[i] = true;
                }
            }  
        } 

        visited[node] = true;
        path.remove(node);
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        isCycle = new boolean[N + 1];
        visited = new boolean[N + 1];
        path = new HashSet<>();

        for (int i = 1; i < N + 1; i++) {
            if (visited[i]) continue;
            dfs(i);
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            if (isCycle[i]) {
                result.add(i);
            }
        }

        Collections.sort(result);
        System.out.println(result.size());
        for (int r : result) {
            System.out.println(r);
        }
    }
}
