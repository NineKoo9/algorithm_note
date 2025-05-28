package 숨바꼭질;

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int K;
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{N, 0});

        boolean[] visited = new boolean[100001];
        visited[N] = true;

        while (!q.isEmpty()) {
            int[] element = q.poll();
            int curNode = element[0];
            int curSec = element[1];
            if (curNode == K) {
                System.out.println(curSec);
                break;
            }

            for (int nextNode : new int[]{curNode + 1, curNode - 1, curNode * 2}) {
                if (nextNode < 0 || nextNode > 100000 || visited[nextNode]) continue;
                visited[nextNode] = true;
                q.offer(new int[]{nextNode, curSec + 1});
            }
        }
    }
}
