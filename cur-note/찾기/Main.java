import java.io.*;
import java.util.*;

public class Main {
        public static int[] failure(String s) {
        int lstSize = s.length();
        int[] f = new int[lstSize];

        // 이제부터 lst의 실패함수를 만들어보자.
        int j = 0;
        for (int i = 1; i < lstSize; i++) {
            while (j > 0 && s.charAt(i) != s.charAt(j)) {
                j = f[j - 1];
            }
            if (s.charAt(i) == s.charAt(j)) {
                j++;
                f[i] = j;
            }
        }
        return f;
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String T = br.readLine();
        String P = br.readLine();

        int n = T.length();
        int m = P.length();

        int[] failfuncP = failure(P);

        int ans = 0;
        List<Integer> points = new ArrayList<>();
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j > 0 && T.charAt(i) != P.charAt(j)) {
                j = failfuncP[j - 1]; // 패턴이 동일한지 찾고 있는데 다르다? 근데 지금까지 찾은 부분에서 끝부분이 앞으로 찾아야할 부분의 첫 부분과 동일하니(있을 수 있고 없을 수 있다.) 그 만큼은 건너뛰자로 봐야한다.
            }

            if (T.charAt(i) == P.charAt(j)) {
                j++;
            }
            if (j == m) {
                ans += 1;
                points.add(i - m + 2);
                // j = 0;
                // i = i - m + 1;
                j = failfuncP[j - 1]; // 이렇게 해야 실패함수를 효율적으로 활용할 수 있다.
            }
        }
        System.out.println(ans);
        StringBuilder sb = new StringBuilder();
        for (int point : points) {
            sb.append(point).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
