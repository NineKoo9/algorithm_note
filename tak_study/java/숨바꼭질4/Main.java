package 숨바꼭질4;

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int K;
    static boolean[] visited;
    static int[] prevTable;
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        prevTable = new int[100001];
        for (int i = 0; i < 100001; i++) {
            prevTable[i] = i;
        }

        visited = new boolean[100001];
        
        Queue<Pair> q = new LinkedList<>();
        visited[N] = true;
        q.offer(new Pair(N, 0));

        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int curNode = pair.node;
            int curSec = pair.sec;

            if (curNode == K) {
                System.out.println(curSec);
                break;
            }

            for (int nextNode : new int[]{curNode + 1, curNode - 1, curNode * 2}) {
                if (nextNode < 0 || nextNode >= 100001 || visited[nextNode]) {
                    continue;
                }
                visited[nextNode] = true;
                prevTable[nextNode] = curNode;
                q.offer(new Pair(nextNode, curSec + 1));
            }
        }

        // 이제 경로를 역추적한다.
        List<Integer> path = new ArrayList<>();
        for (int i = K; i != prevTable[i]; i = prevTable[i]) {
            path.add(i);
        }
        path.add(N);

        StringBuilder sb = new StringBuilder();
        for (int i = path.size() - 1; i >= 0; i--) {
            sb.append(path.get(i));
            if (i != 0) {
                sb.append(" ");
            }
        }

        System.out.println(sb.toString());
        
    }

    static class Pair {
        int node;
        int sec;

        public Pair(int node, int sec) {
            this.node = node;
            this.sec = sec;
        }

       @Override
       public String toString() {
        return "(node=" + node + ", " + "sec=" + sec + ")";
       }
    }
    
}
