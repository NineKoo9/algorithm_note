package 파일명정렬;

import java.util.*;

class myComparator implements Comparator<String> {

    public int[] getNumRange(String s){
        int[] range = new int[2];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                range[0] = i;
                while (i + 1 < s.length() && Character.isDigit(s.charAt(i + 1))) {
                    i += 1;
                }
                range[1] = i;
                break;
            }
        }
        return range;
    }

    @Override
    public int compare(String s1, String s2) {
        // 여기서부터 문자열 슬리이싱을 해나가야한다.
        s1 = s1.toLowerCase();
        s2 = s2.toLowerCase();
        int[] s1NumRange = getNumRange(s1);
        int[] s2NumRange = getNumRange(s2);
        int cmp1 = s1.substring(0, s1NumRange[0]).compareTo(s2.substring(0, s2NumRange[0]));
        if (cmp1 != 0) return  cmp1;
        String subS1 = s1.substring(s1NumRange[0], s1NumRange[1] + 1);
        String subS2 = s2.substring(s2NumRange[0], s2NumRange[1] + 1);
        return Integer.parseInt(subS1) - Integer.parseInt(subS2);
    }
}

class Solution {
    public String[] solution(String[] files) {
        List<String> filesLst = Arrays.asList(files);
        filesLst.sort(new myComparator());
        return filesLst.toArray(String[]::new);
    }
}