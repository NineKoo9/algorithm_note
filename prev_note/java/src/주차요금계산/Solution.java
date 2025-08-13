package 주차요금계산;

import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        final int ENDTIME = 23 * 60 + 59;
        int defaultTime = fees[0];
        int defaultFee = fees[1];
        int unitTime = fees[2];
        int unitFee = fees[3];
        Map<String, Integer> carTotalMap = new HashMap<>();
        for (String record : records) {
            int time = 60 * Integer.parseInt(record.substring(0,2)) + Integer.parseInt(record.substring(3,5));
            String carName = record.substring(6, 10);
            String status = record.substring(11);
            if (status.equals("IN")) {
                if (!carTotalMap.containsKey(carName)) {
                    carTotalMap.put(carName, ENDTIME - time);
                } else {
                    carTotalMap.replace(carName, carTotalMap.get(carName) + ENDTIME - time);
                }
            } else {
                carTotalMap.replace(carName, time - ENDTIME + carTotalMap.get(carName));
            }
        }
        List<Integer> answer = new ArrayList<>();
        List<String> keys = new ArrayList<>(carTotalMap.keySet());
        keys.sort((s1, s2) -> s1.compareTo(s2));
        for (String key: keys) {
            int total = carTotalMap.get(key);
            if (total > defaultTime) {
                answer.add(defaultFee + ((int) Math.ceil((double)(total - defaultTime)/unitTime)) * unitFee);
                continue;
            }
            answer.add(defaultFee);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] fees = {180, 5000, 10, 600};
        String[] records = {"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"};
        System.out.println(sol.solution(fees, records));
    }
}