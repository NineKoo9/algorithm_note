package 합이0인네정수;

import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] A = new int[N], B = new int[N], C = new int[N], D = new int[N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            A[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(st.nextToken());
            C[i] = Integer.parseInt(st.nextToken());
            D[i] = Integer.parseInt(st.nextToken());
        }

        int size = N * N;
        int[] sums1 = new int[size], sums2 = new int[size];
        int idx = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sums1[idx] = A[i] + B[j];
                sums2[idx] = C[i] + D[j];
                idx++;
            }
        }

        Arrays.sort(sums1);
        Arrays.sort(sums2);

        long cnt = 0;
        int i = 0, j = size - 1;
        while (i < size && j >= 0) {
            int s = sums1[i] + sums2[j];
            if (s == 0) {
                int v1 = sums1[i], c1 = 0;
                while (i < size && sums1[i] == v1) {
                    c1++;
                    i++;
                }
                int v2 = sums2[j], c2 = 0;
                while (j >= 0 && sums2[j] == v2) {
                    c2++;
                    j--;
                }
                cnt += (long)c1 * c2;
            }
            else if (s < 0) {
                i++;
            }
            else {
                j--;
            }
        }

        System.out.println(cnt);
    }
}
