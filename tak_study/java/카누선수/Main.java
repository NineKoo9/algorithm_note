package 카누선수;

import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int stage = 0; stage < T; stage++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());  // 보트의 특정값
            int n = Integer.parseInt(st.nextToken()); // 학생 수

            int[][] classMatrix = new int[4][n];

            for (int i = 0; i < 4; i ++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    classMatrix[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int size = n * n;
            long[] sum12 = new long[size];
            long[] sum34 = new long[size];
            int seq = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    sum12[seq] = classMatrix[0][i] + classMatrix[1][j];
                    sum34[seq] = classMatrix[2][i] + classMatrix[3][j];
                    seq++;
                }
            }

            Arrays.sort(sum12);
            Arrays.sort(sum34);

            long answerValue = 0;
            long minDiff = Integer.MAX_VALUE;

            int idx12 = 0;
            int idx34 = size - 1;
            while (idx12 < size && idx34 >= 0) {
                long s1234 = sum12[idx12]+ sum34[idx34];
                long diff = Math.abs(k - s1234);

                if (diff < minDiff || (diff == minDiff && s1234 < answerValue)) {
                    minDiff = Long.min(minDiff, diff);
                    answerValue = s1234;
                }

                if (s1234 == k) {
                    break;
                } else if (s1234 < k) {
                    idx12++;
                } else if (s1234 > k) {
                    idx34--;
                }
            }

            System.out.println(answerValue);
        }
    }
}
