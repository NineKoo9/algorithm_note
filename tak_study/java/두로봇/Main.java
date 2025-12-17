package 두로봇;

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int robotPos1;
    static int robotPos2;
    static List<List<int[]>> graph;
    static boolean[] visited;
    static int[] resultPath;

    public static void dfs(int node, List<Integer> path) {
        visited[node] = true;
        if (node == robotPos2) {
            resultPath = new int[path.size()];
            for (int i = 0; i < path.size(); i++) {
                resultPath[i] = path.get(i);
            }
            return;
        }

        for (int[] element : graph.get(node)) {
            int nextNode = element[0];
            int nextDist = element[1];
            if (visited[nextNode]) continue;
            path.add(nextDist);
            dfs(nextNode, path);
            path.remove(path.size() - 1);
        }
        return;
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        robotPos1 = Integer.parseInt(st.nextToken());
        robotPos2 = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());
            graph.get(v1).add(new int[]{v2, dist});
            graph.get(v2).add(new int[]{v1, dist});
        }


        visited = new boolean[N + 1];
        dfs(robotPos1, new ArrayList<>());
        Arrays.sort(resultPath);
        int answer = 0;
        for (int i = 0; i < resultPath.length - 1; i++) {
            answer += resultPath[i];
        }
        System.out.println(answer);
    }
}
