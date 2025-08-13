package 펠린드롬분할;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();

        int N = S.length();

        // 한번에 모두 구하기보단... 특정 범위의 값이 팰린드롬인지 아닌지 미리 구해놓는 것이 좋구나?
        boolean[][] isPal = new boolean[N][N];
        for (int l = 1; l <= N; l++) {
            for (int i = 0; i <= N - l; i++) {
                int j = i + l - 1;
                isPal[i][j] = S.charAt(i) == S.charAt(j) && (l <= 2 || isPal[i+1][j-1]);
            }
        }

        int[] dp = new int[N + 1]; // dp[i] : s[i … n-1](뒤쪽 접미사)의 최소 팔린드롬 조각 수
        Arrays.fill(dp, N);
        dp[N] = 0; // 인덱스 범위를 벗어나는 경우 때문에 이것이 필요하다.
        for (int i = N - 1; i >= 0; i--) {
            for (int j = i; j < N; j++) {
                if (isPal[i][j]) {
                    dp[i] = Math.min(dp[i], 1 + dp[j + 1]);
                }
            }
        }
        System.out.println(dp[0]);
    }
}
