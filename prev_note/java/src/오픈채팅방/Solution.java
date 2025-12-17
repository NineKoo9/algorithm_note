package 오픈채팅방;
import java.util.*;

class Solution {
    public String[] solution(String[] records) {
        Map<String, String> uidMap = new HashMap<String, String>();
        List<String[]> results = new ArrayList<>();
        Map<String, String> statusMap = Map.of("Leave", "나갔습니다.", "Enter", "들어왔습니다.");
        for (String record: records) {
            String[] recordInfo = record.split(" ");
            if (!recordInfo[0].equals("Change")) {
                String[] s = {recordInfo[0], recordInfo[1]}; // enter , uid
                results.add(s); 
            }
            if (!recordInfo[0].equals("Leave")) {
                uidMap.put(recordInfo[1], recordInfo[2]);
            }
        }
        String[] answer = new String[results.size()];
        for (int i = 0; i < answer.length; i++) {
            String[] result = results.get(i);
            answer[i] = uidMap.get(result[1]) + "님이 " + statusMap.get(result[0]);
        }
        return answer;
    }
}

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
        System.out.println(Arrays.toString(sol.solution(record)));
    }
}