package 재활용캠페인;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static int N;
    static long X;
    static long[] C;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        X = Long.parseLong(st.nextToken());

        C = new long[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            C[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(C);
        List<Long> cList = Arrays.stream(C).boxed().collect(Collectors.toList());
        
        int ans = 0;
        for (int i = cList.size() - 1; i >= 0; i--) {
            if (cList.get(i) >= X) {
                ans++;
                cList.remove(i);
            }
        }
        System.out.println(cList);

        int lo = 0;
        int hi = cList.size() - 1;
        int rest = cList.size();
        while (lo < hi) {
            if (cList.get(lo) + cList.get(hi) >= (X + 1) / 2) { // 어쨋든 합이 둘다 정수이고... x가 홀수인 경우 0.5를 잃어버리는 것이 문제니까 안전하게 (X + 1) / 2로 하자
                ans++;
                lo++;
                hi--;
                rest -= 2;
            } else {
                lo++;
            }
        }
        
        System.out.println(ans + rest / 3);
    }
}
