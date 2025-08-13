import java.io.*;
import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(String[] gems) {
        // 모든 보석을 하나 이상 포함하는 가장 짧은 구간.
        // 즉 특정 구간까지 보석이 몇개 있는지 체크해야한다?
        // 일단 어떤 보석들이 있는지 체크할까?
        int allCount = Arrays.stream(gems).distinct().collect(Collectors.toList()).size();
        Map<String, Integer> pocket = new HashMap<>();
        
        int minLength = 100001;
        int[] ans = {};
        int start = 0;
        for (int end = 0; end < gems.length; end++) {
            String gem = gems[end];
            pocket.merge(gem, 1, Integer::sum);

            while (pocket.keySet().size() == allCount) {
                if (end - start + 1 < minLength) {
                    ans = new int[]{start + 1, end + 1};
                    minLength = end - start + 1;
                }

                // 이제 앞의 녀석을 하나 빼준다.
                String firstGem = gems[start];
                pocket.put(firstGem, pocket.get(firstGem) - 1);
                // 근데 만약 0이라면? 키를 제거해줘야한다.
                if (pocket.get(firstGem) == 0) {
                    pocket.remove(firstGem);
                }
                start += 1;
            } 
        }

        return ans;
    }
}