package 최단경로;

import java.io.*;
import java.util.*;

public class Main {
    static int V;  // 1~20000
    static int E;  // 1~300000
    static int start;
    static List<List<int[]>> graph;
    static int[] dp;
    static final int INF = (int) 1e9;

    public static void dijkstra(int node) {
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        dp[node] = 0;
        pq.offer(new Pair(node, 0));
        
        while (!pq.isEmpty()) {
            Pair pair = pq.poll();
            int curNode = pair.node;
            int curCost = pair.cost;

            if (dp[curNode] < curCost) continue;

            for (int[] element : graph.get(curNode)) {
                int nextNode = element[0];
                int nextCost = element[1];
                if (dp[nextNode] > curCost + nextCost) {
                    dp[nextNode] = curCost + nextCost;
                    pq.offer(new Pair(nextNode, curCost + nextCost));
                }
            }
        }
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        start = Integer.parseInt(br.readLine());

        graph = new ArrayList<>();
        for (int i = 0; i < V + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(u).add(new int[]{v, w});
        }

        dp = new int[V + 1];
        Arrays.fill(dp, INF);

        dijkstra(start);
        for (int i = 1; i < V + 1; i++) {
            System.out.println(dp[i] != INF ? dp[i] : "INF");
        }
    }
    
    static class Pair implements Comparable<Pair>{
        int node;
        int cost;

        Pair(int node, int cost) {
            this.node = node;
            this.cost = cost;
        }

        @Override
        public String toString() {
            return "(" + "node:" + node + ", " + "cost:" + cost + ")";
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pair other = (Pair) o;
            return node == other.node && cost == other.cost;
        }

        @Override
        public int compareTo(Pair other) {
            return Integer.compare(this.cost, other.cost);
        }
    };
}
