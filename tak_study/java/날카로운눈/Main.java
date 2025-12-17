package 날카로운눈;

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[][] integerDummy;

    // 특정값 m이하의 수가 홀수개인지 체크한다.
    public static long getLessThanEqual(long m) {
        long totalCnt = 0;
        for (int i = 0; i < N; i++) {
            long A = integerDummy[i][0], C = integerDummy[i][1], B = integerDummy[i][2];
            if (m < A) continue;                
            long k = (m - A) / B + 1;            
            long maxK = (C - A) / B + 1;
            totalCnt += Math.min(k, maxK);  
        }
        return totalCnt;
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        integerDummy = new int[N][3];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                integerDummy[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        long s = 0;
        long e = 2147483647;
        Object ansValue = "NOTHING";
        long ansCount = 0;
        while (s <= e) {
            long mid = (s + e) / 2;
            long lessThanEqualCount = getLessThanEqual(mid);
            if (lessThanEqualCount % 2 != 0) {
                long lessThanCount = getLessThanEqual(mid - 1);
                ansValue = mid;
                ansCount = lessThanEqualCount - lessThanCount;
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }

        if (ansValue == "NOTHING") {
            System.out.println(ansValue);
        } else {
            System.out.print(ansValue);
            System.out.print(" " + ansCount);
        }
    }
}
