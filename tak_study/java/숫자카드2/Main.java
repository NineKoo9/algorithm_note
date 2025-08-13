package 숫자카드2;

import java.io.*;
import java.util.*;

public class Main {
    public static int N;
    public static int[] cards;
    public static int M;
    public static int[] targets;

    // 아쉽게도 이 풀이는 시간초과가 발생한다.
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

        for (int target : targets) {
            // target을 cards에 몇개를 가지고 있는지 찾아야한다.

            // 먼저 LowerBound을 찾자.
            int s = 0;
            int e = N - 1;
            int lower = 0;
            while (s == e || s < e) {
                int mid = (s + e) / 2;
                if (cards[mid] < target) {
                    s = mid + 1;
                } else {
                    lower = mid;
                    e = mid - 1;
                }
            }

            // 이제 upperBound을 찾자.
            s = 0;
            e = N - 1;
            int upper = N;
            while (s == e || s < e) {
                int mid = (s + e) / 2;
                if (cards[mid] > target) {
                    upper = mid;
                    e = mid - 1;
                } else {
                    s = mid + 1;
                }
            }
            int cnt = upper - lower;
            System.out.print(cnt);
            System.out.print(" ");
        }
    }

    public static void main2(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        Map<Integer, Integer> myCards = new HashMap<>();
        for (int i = 0; i < N; i++) {
            int card = Integer.parseInt(st.nextToken());
            myCards.put(card, myCards.getOrDefault(card, 0) + 1);
        }
        
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            int query = Integer.parseInt(st.nextToken());
            sb.append(myCards.getOrDefault(query, 0)).append(' ');
        }
        
        System.out.println(sb.toString().trim());
    }
}
