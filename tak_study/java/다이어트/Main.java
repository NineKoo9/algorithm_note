package 다이어트;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int G = Integer.parseInt(br.readLine().trim());

        List<Integer> answers = new ArrayList<>();

        int l = 1, r = 2;
        while (l < r) {
            int diff = r*r - l*l;
            if (diff == G) {
                answers.add(r);
                l++;       
            }
            else if (diff < G) {
                r++;       
            }
            else {
                l++;       
            }
        }

        if (answers.isEmpty()) {
            System.out.println(-1);
        } else {
            StringBuilder sb = new StringBuilder();
            for (int w : answers) {
                sb.append(w).append('\n');
            }
            System.out.print(sb);
        }
    }
}