import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken()) % M;
        }

        long[] prefixSum = new long[N + 1];
        Map<Long, Long> countMap = new HashMap<>();
        for (int i = 1; i < N + 1; i++) {
            prefixSum[i] = prefixSum[i - 1] + A[i - 1];
            Long r = prefixSum[i] % M;
            countMap.merge(r, 1L, Long::sum);
        }
        long ans = countMap.getOrDefault(0L, 0L);
        for (long v : countMap.values()) {
            ans += (v * (v - 1)) / 2;
        }
        System.out.println(ans);
    }
}
