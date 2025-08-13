package 작은벌점;

import java.io.*;
import java.util.*;

public class Main {
    public static int getLowerBound(int[] arr, int target) {
        // 빈 배열 처리
        if (arr.length == 0) {
            return 0;
        }
        
        int lower = arr.length; // 모든 원소가 target보다 작은 경우를 대비해 배열 길이로 초기화
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2; // 오버플로우 방지
            
            if (arr[mid] >= target) {
                lower = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return lower;
    }

    // 이 코드는 잘못된 풀이다.
    public static void main2(String[] args) throws Exception {
        BufferedReader br  =new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int[][] playerCards = new int[3][];
        playerCards[0] = new int[A];
        playerCards[1] = new int[B];
        playerCards[2] = new int[C];

        int[] counts = {A, B, C};
        for (int player = 0; player < 3; player++) {
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < counts[player]; i++) {
                playerCards[player][i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(playerCards[player]);
        }

        // 3개의 배열에서 가장 큰 min을 어떻게 구하지?
        int maxMinIdx = 0;
        for (int i = 1; i < 3; i++) {
            if (playerCards[i][0] > playerCards[maxMinIdx][0]) {
                maxMinIdx = i;
            }
        }

        // maxMinIdx 에서 Min을 가지는 것으로 하고 이제 minMax을 구하자.
        int ans = Integer.MAX_VALUE;

        for (int minValue : playerCards[maxMinIdx]) {
            int arrIdx1 = (maxMinIdx + 1) % 3;
            int arrIdx2 = (maxMinIdx + 2) % 3;
            int value1 = playerCards[arrIdx1][getLowerBound(playerCards[arrIdx1], minValue)];
            int value2 = playerCards[arrIdx2][getLowerBound(playerCards[arrIdx2], minValue)];
            int maxValue = Math.max(value1, value2);

            if (minValue > maxValue) continue;
            ans = Math.min(ans, maxValue - minValue);
        }
        
        System.out.println(ans);
    }
}
