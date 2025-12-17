package 실패율;

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int N, int[] stages) {
        List<Integer> stagesSorted = Arrays.stream(stages).boxed().sorted().collect(Collectors.toList());
        Map<Integer, Integer> stageCount = new HashMap<>();
        for (int stage : stagesSorted) {
            stageCount.put(stage, stageCount.getOrDefault(stage, 0) + 1);
        }
        Map<Integer, Double> stageFailRate = new HashMap<>();
        int total = stages.length;
        for (int stage = 1; stage <= N; stage++) {
            int completedPersons = stageCount.getOrDefault(stage, 0);
            stageFailRate.put(stage, ((double) completedPersons/total));
            total -= completedPersons;
        }
        List<Integer> answer = new ArrayList<>(stageFailRate.keySet());
        answer.sort((a, b) -> {
            if (stageFailRate.get(a) > stageFailRate.get(b)) return -1;
            if (stageFailRate.get(a) < stageFailRate.get(b)) return 1;
            return a - b;
        });
        return answer.stream().mapToInt(i -> i).toArray();
    }
}

// N은 1 이상 500 이하의 자연수입니다.
// stages의 길이는 1 이상 200,000 이하입니다.


class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int N = 5;
        int[] stages = {2, 1, 2, 6, 2, 4, 3, 3};
        System.out.println(Arrays.toString(sol.solution(N, stages)));
    }
}