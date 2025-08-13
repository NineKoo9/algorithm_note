package 섞기수열;

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[] arr;
    static int[] parentTable;

    public static int findParent(int node) {
        if (parentTable[node] == node) {
            return node;
        }
        parentTable[node] = findParent(parentTable[node]);
        return parentTable[node];
    }

    public static boolean union(int nodeA, int nodeB) {
        int parentA = findParent(nodeA);
        int parentB = findParent(nodeB);
        if (parentA == parentB) {
            return false;
        }
        if (parentA > parentB) {
            parentTable[parentA] = parentB;
        } else {
            parentTable[parentB] = parentA;
        }
        return true;
    }

    public static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static long lcm(long a, long b) {
        return (a * b) / (a > b ? gcd(a, b) : gcd(b, a));
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 이제 여기서 사이클을 처리해야하는데... 그래프로 처리할까?
        // 원래대로 돌아온다니끼 각 노드들은 반드시 사이클안에 포함되어 있다. 그렇다면 각 집합의 크기만 구하면 될듯?
        parentTable = new int[N + 1];
        for (int i = 0; i < N + 1; i++) {
            parentTable[i] = i;
        }

        // 이제부터 부모테이블을 초기화하자.
        for (int i = 0; i < N; i++) {
            int a = i + 1;
            int b = arr[i];
            // a와b 두 노드를 같은 집합에다가 넣어야지?
            union(a, b);
        }

        Map<Integer, Integer> counter = new HashMap<>();
        // 자 이제 부모테이블이 초기화되었을테니까 각 노드별로 최소공배수를 구하면 될텐데 이것도 조금 더 최적화할 수 있지 않을까?
        for (int i = 1; i < N + 1; i++) {
            int p = findParent(i);
            counter.put(p, 1 + counter.getOrDefault(p, 0));
        }

        // 이제 모든 value들의 최소공배수를 구하면 되겠다. 최소 공배수는 어떻게 구하지? 모든 곱에다가 최대공약수를 나눠주면 되나?
        // 흠... 최소공배수를 구하는 것이 쉽지않구나
        // List<Long> values = new ArrayList<>(counter.values());
        // while (values.size() >= 2) {
        //     int a = values.remove(values.size() - 1);
        //     int b = values.remove(values.size() - 1);
        //     values.add(lcm(a, b));
        // }
        long answer = 1;
        for (int value : counter.values()) {
            answer = lcm(answer, value);

        }


        System.out.println(answer);

    }
    
}
