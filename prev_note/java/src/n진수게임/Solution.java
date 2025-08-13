package n진수게임;


class Solution {
    public String solution(int n, int t, int m, int p) {
        StringBuilder nums = new StringBuilder();
        for (int i = 0; nums.length() <= t * m; i++) {
            nums.append(Integer.toString(i, n));
        }
        StringBuilder answer = new StringBuilder();
        // 그렇다면 올라가는 이 숫자를 어떻게 정의할까?
        for (int i = 1; answer.length() < t; i++){
            if ((i - p) % m == 0) {
                answer.append(nums.charAt(i - 1));
            }
        }
        return answer.toString().toUpperCase();
    }
}