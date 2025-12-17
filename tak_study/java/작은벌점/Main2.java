package 작은벌점;

import java.io.*;
import java.util.*;

public class Main2 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int[][] playerCards = new int[3][];
        playerCards[0] = new int[A];
        playerCards[1] = new int[B];
        playerCards[2] = new int[C];

        int[] counts = {A, B, C};
        for (int player = 0; player < 3; player++) {
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < counts[player]; i++) {
                playerCards[player][i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(playerCards[player]);
        }

        int i = 0, j = 0, k = 0;
        int answer = Integer.MAX_VALUE;

        while (i < A && j < B && k < C) {
            int x = playerCards[0][i], y = playerCards[1][j], z = playerCards[2][k];
            int curMax = Math.max(x, Math.max(y, z));
            int curMin = Math.min(x, Math.min(y, z));
            answer = Math.min(answer, curMax - curMin);

            if (answer == 0) break;

            if (curMin == x) i++;
            else if (curMin == y) j++;
            else k++;
        }
        System.out.println(answer);
    }
}
