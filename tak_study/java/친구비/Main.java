package 친구비;

import java.util.*;
import java.io.*;

public class Main {
    static int studentNum;
    static int relationNum;
    static int initMoney;
    static int[][] friendTable;
    static Map<Integer, Integer> groupMap;

    public static int findFriend(int child) {
        if (child == friendTable[child][0]) {
            return child;
        }

        int friend = findFriend(friendTable[child][0]);
        friendTable[child][0] = friend;
        return friend;
    }

    public static void union(int child1, int child2) {
        int friend1 = findFriend(child1);
        int friend2 = findFriend(child2);
        if (friend1 == friend2) {
            return;
        } else if (friend1 > friend2) {
            friendTable[friend1][0] = friend2;
        } else if (friend1 < friend2) {
            friendTable[friend2][0] = friend1;
        }
        return;
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        studentNum = Integer.parseInt(st.nextToken());
        relationNum = Integer.parseInt(st.nextToken());
        initMoney = Integer.parseInt(st.nextToken());

        friendTable = new int[studentNum + 1][2];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < studentNum + 1; i++) {
            friendTable[i][0] = i;
            friendTable[i][1] = Integer.parseInt(st.nextToken());
        }

        // 자 이제 각 관계에 대해서 그룹화를 한다.
        for (int i = 0; i < relationNum; i++) {
            st = new StringTokenizer(br.readLine());
            int s1 = Integer.parseInt(st.nextToken());
            int s2 = Integer.parseInt(st.nextToken());
            union(s1, s2);
        }

        // 이제 만들어진 친구관계에서 최소비용을 구해야한다.
        groupMap = new HashMap<>();
        for (int i = 1; i < studentNum + 1; i++) {
            int root = findFriend(i);
            int groupFee = friendTable[i][1];
            groupMap.put(root, Math.min(groupFee, groupMap.getOrDefault(root, groupFee)));
        }
        
        int ans = 0;
        for (int v : groupMap.values()) {
            ans += v;
        }
        System.out.println(ans <= initMoney ? ans : "Oh no");
    }
}
