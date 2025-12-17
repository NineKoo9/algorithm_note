package 보석상자;

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[] jewels;

    public static int getChildCnt(int m) {
        int cnt = 0;
        for (int i = 0; i < M; i++) {
            cnt += (int) Math.ceil((double) jewels[i] / m);
        }
        return cnt;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        jewels = new int[M];
        for (int i = 0; i < M; i++) {
            jewels[i] = Integer.parseInt(br.readLine());
        }

        int s = 0;
        int e = (int) 1e9;
        int ans = 0;
        while ( s <= e) {
            int mid = (s + e) / 2;
            int childCnt = getChildCnt(mid);
            if (childCnt <= N) {
                ans = mid;
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }

        System.out.println(ans);
    }
}
