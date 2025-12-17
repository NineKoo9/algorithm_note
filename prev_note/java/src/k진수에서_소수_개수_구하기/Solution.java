package k진수에서_소수_개수_구하기;

class Solution {
    public int solution(int n, int k) {
        // 먼저 n을 k 진수로 바꿔볼까?
        StringBuilder k_jinsu = new StringBuilder();
        while (n > 0) {
            k_jinsu.insert(0, n % k);
            n = n/k;
        }
        String[] prime_candidates = k_jinsu.toString().split("0");
        int answer = 0;
        for (String primeCandidate : prime_candidates) {
            if (primeCandidate.isEmpty()) continue;
            if (is_prime(Long.parseLong(primeCandidate))) answer++;
        }
        return answer;
    }

    private boolean is_prime(long num) {
        if (num < 2) return false;
        for (long i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int n = 437674;
        int k = 3;
        System.out.println(sol.solution(n, k));
    }
}
