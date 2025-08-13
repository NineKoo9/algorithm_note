package 압축;

import java.util.*;

class Solution {
    public String findMax(int start, String msg, Map<String, Integer> dic) {
        for (int end = msg.length(); end >= start; end--) {
            String subStr = msg.substring(start, end);
            if (dic.containsKey(subStr)) return subStr;
        }
        return msg.substring(start);
    }
    public int[] solution(String msg) {
        int idx_num = 1;
        char word = 'A';
        Map<String, Integer> dictionary = new HashMap<>();
        for (; idx_num <=26; idx_num++){
            dictionary.put((word++) + "", idx_num);
        }
        System.out.println(dictionary);
        // 색이되는 길이가 점점 길어질 수 있는데 어떻게 처리할까?
        List<Integer> answer = new ArrayList<>();
        int idx = 0;
        while (idx< msg.length()) {
            String subString = findMax(idx, msg, dictionary);
            answer.add(dictionary.get(subString));
            int next_idx = idx + subString.length();
            if (next_idx + 1 < msg.length()) {
                dictionary.put(msg.substring(idx, next_idx + 1), idx_num++);
            }
            idx = next_idx;
        }
        System.out.println("dictionary = " + dictionary);
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String msg = "KAKAO";
        System.out.println(Arrays.toString(sol.solution(msg)));
    }
}