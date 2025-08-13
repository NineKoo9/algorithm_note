package 숫자카드;

import java.io.*;
import java.util.*;

public class Main {
    public static int N;
    public static int[] cards;
    public static int M;
    public static int[] targets;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        cards = new int[N];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(cards);

        M = Integer.parseInt(br.readLine());
        targets = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            targets[i] = Integer.parseInt(st.nextToken());
        }

        StringBuilder answer = new StringBuilder();
        for (int target : targets) {
            int s = 0;
            int e = N - 1;
            int ans = 0;
            
            while (s == e || s < e) {
                int mid = (s + e) / 2;
                if (cards[mid] == target) {
                    ans = 1;
                    break;
                } else if (cards[mid] < target) {
                    s = mid + 1;
                } else {
                    e = mid - 1;
                }
            }
            answer.append(ans + " ");
        }
        System.out.println(answer);
    }
}
