import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        int[] A = new int[N];
        int[] B = new int[M];
        
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }
        
        StringBuilder sb = new StringBuilder();
        int i = 0, j = 0;
        while (i < N && j < M) {
            if (A[i] <= B[j]) {
                sb.append(A[i++]).append(' ');
            } else {
                sb.append(B[j++]).append(' ');
            }
        }
        while (i < N) sb.append(A[i++]).append(' ');
        while (j < M) sb.append(B[j++]).append(' ');
        
        System.out.println(sb.toString().trim());

    }
}
