package 용액;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] liquidArr = new int[N];
        for (int i = 0; i < N; i++) {
            liquidArr[i] = Integer.parseInt((st.nextToken()));
        }

        // 이미 정렬된 것이 주어짐
        int s = 0, e = N - 1;
        int minDiff = Integer.MAX_VALUE;
        int a1 = 0, a2 = 0;
        while (s < e) {
            int composite = liquidArr[s] + liquidArr[e];
            int diff = Math.abs(0 - composite);

            if (diff < minDiff) {
                minDiff = Math.min(minDiff, diff);
                a1 = liquidArr[s];
                a2 = liquidArr[e];
            }

            if (composite == 0) {
                break;
            } else if (composite < 0) {
                s++;
            } else if (composite > 0) {
                e--;
            }
        }

        System.out.println(a1 + " " + a2);
    }
}
