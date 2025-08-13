package 서프라이즈;

import java.io.*;
import java.util.*;

// 하 계속 75퍼에서 틀린다...
public class Main {
    static int N;
    static int[] steakWeights;

    static public int upperBound(int[] arr, int s, int e, int num) {
        int ans = e + 1;
        int start = s;
        int end = e;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] > num) {
                ans = mid;
                end = mid - 1;
            }
            else if (arr[mid] <= num) { // 만약 여기서 조건문이 실행되고 start == end인 경우 반복문을 종료해버리면, 중복된 Num이 있는 경우 ans가 제대로 갱신되지 않을 확률이 있어.
                start = mid + 1;
            }
        }
        return ans;
    }

    static public int lowerBound(int[] arr, int s, int e, int num) {
        int ans = e + 1;
        int start = s;
        int end = e;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] >= num) {
                ans = mid;
                end = mid - 1;

            }
            else if (arr[mid] < num) {
                start = mid + 1;
            }
        }
        return ans;
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        
        steakWeights = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            steakWeights[i] = Integer.parseInt(st.nextToken());
        }

        // 일단 최적화를 위해 누적합을 구하자.
        int[] prefixSum = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            prefixSum[i] = steakWeights[i - 1] + prefixSum[i - 1];
        }

        int E = Integer.MAX_VALUE;
        int ans = 0;
        for (int length = 2; length <= N; length++) {
            for (int i = 0; i <= N - length; i++) {
                // 이제부터 i~k, k+1 ~j 까지의 비교가 필요하다.
                // 여기 이 부분을 최적화해서 이분탐색으로 바꿀 수 있다. 처음부터 끝까지 k값이 움직이는 것으로는 시간복잡도가 길이 l이 된다.
                int j = i + length - 1;
                int total = prefixSum[j+1] - prefixSum[i];
                int target = prefixSum[i] + total / 2; // 아 이부분이 잘못되었구나... 단순히 half만 하면 잘못되지...
                // 이제부터 half에 가까운 위치를 구하면 된다. 단 k의 위치는 반드시 (i, j-1) 이어야한다.
                int lower = Math.min(j - 1, lowerBound(prefixSum, i, j + 1, target) - 1);
                for (int k = lower; k <= lower + 1; k++) {
                    if (k < i || k >= j) {
                        continue;
                    }
                    int calcE = Math.abs((prefixSum[k + 1] - prefixSum[i]) - (prefixSum[j + 1] - prefixSum[k + 1]));
                    int calcAns = (prefixSum[k + 1] - prefixSum[i]) + (prefixSum[j + 1] - prefixSum[k + 1]);
                    if (calcE < E) { // E가 더 작아졌을 때는 ans를 덮어써야 합니다. <= 으로 처리하면 차이는 줄었는데 → 앞서 저장해 둔 더 큰 총합이 계속 남는 “불일치” 케이스가 생길 수 있다.
                        E = calcE;
                        ans = calcAns;
                    } else if (calcE == E) {
                        ans = Math.max(ans, calcAns);
                    }
                }
                
            }
        }
        System.out.println(ans);
        
    }
    
}
