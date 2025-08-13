package 소수의연속합;

import java.util.*;
import java.io.*;

public class Main {
    public static boolean checkPrime(int num) {
        for (int i = 2; i < Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        boolean[] isPrime = new boolean[N + 1];
        Arrays.fill(isPrime, true);

        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i < N + 1; i++) {
            if (isPrime[i] == true && checkPrime(i)) {  // 업데이트되지 않았고 소수라면?
                for (int j = 2; i * j < N + 1; j++ ) {
                    isPrime[i * j] = false;
                }
            }
        }

        List<Integer> primeNums = new ArrayList<>();
        for (int i = 2; i < N + 1; i++) {
            if (isPrime[i]) {
                primeNums.add(i);
            }
        }
        int size = primeNums.size();

        int[] prefixSums = new int[size + 1];
        Arrays.fill(prefixSums, 0);
        for (int i = 1; i < size + 1; i++) {
            prefixSums[i] = prefixSums[i - 1] + primeNums.get(i - 1);
        }

        int s = 0;
        int e = 1;
        int cnt = 0;
        while (s < e && e < size + 1) {
            int consequence_sum = prefixSums[e] - prefixSums[s];
            if (consequence_sum == N) {
                cnt++;
                e++;
            } else if (consequence_sum < N) {
                e++;
            } else {
                s++;
            }
        }
        System.out.println(cnt);
    }
}
