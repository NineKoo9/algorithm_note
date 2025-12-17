import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int S;
    static int[] arr;

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // prefixSum[i] 은 [0, i) 까지의 합이다. 즉 arr[0] + ... + arr[i - 1]
        int[] prefixSum = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
        }

        // arr 중에서 연속된 수들의 합? 미리 구해놓을 수 있으나 이건 최적화니 조금 뒤에 생각하고
        int a = 0;
        int b = 1;
        int ans = (int) 1e6;
        while (a <= b && b < N + 1) {
            int consequnceSum = prefixSum[b] - prefixSum[a]; // [a, b) 까지의 합이다.
            if (consequnceSum >= S) {
                ans = Math.min(ans, b - a);
                a++;
            } else {
                b++;
            }
        }
        System.out.println(ans != (int) 1e6 ? ans : 0);
    }
}
