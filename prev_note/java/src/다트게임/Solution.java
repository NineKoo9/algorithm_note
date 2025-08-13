package 다트게임;

import java.util.*;

class Solution {
    public int solution(String dartResult) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 0 ; i < dartResult.length(); i++) {
            if (Character.isDigit(dartResult.charAt(i))) {
                int num = dartResult.charAt(i) - '0';
                if (Character.isDigit(dartResult.charAt(i+1))) {
                    num = 10;
                    i++;
                }
                char option = i + 2 < dartResult.length() && !Character.isDigit(dartResult.charAt(i+2)) ? dartResult.charAt(i+2) : '0';
                if (option == '*' && !answer.isEmpty()) {
                    answer.set(answer.size() -1, answer.get(answer.size() -1) * 2);
                }
                answer.add(calc(num, dartResult.charAt(i+1), option));
            }
        }
        return answer.stream().reduce(0,Integer::sum);
    }

    static int calc(int num, char bonus, char option) {
        Map<Character, Integer> bonusMap = Map.of('S', 1, 'D', 2, 'T', 3);
        if (! (option == '0')) {
            int result = (int) Math.pow(num, bonusMap.get(bonus));
            return option == '*' ? result * 2 : result * (-1);
        }
        return (int) Math.pow(num, bonusMap.get(bonus));
    }
}

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String dartResult = "1S2D*3T";
        System.out.println(sol.solution(dartResult));
    }
}