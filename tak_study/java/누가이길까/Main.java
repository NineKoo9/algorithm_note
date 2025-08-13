package 누가이길까;

import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] HITeam;
    static int[] ARCTeam;

    private static int lowerBound(int[] arr, int key) {
        int s = 0;
        int e = arr.length - 1;
        int lower = arr.length;
        while ( s <= e) {
            int mid = (s + e) / 2;
            if (arr[mid] >= key) {
                lower = mid;
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }
        return lower;
    }

    private static int upperBound(int[] arr, int key) {
        int s = 0;
        int e = arr.length - 1;
        int upper = arr.length;
        while (s <= e) {
            int mid = (s + e) / 2;
            if (arr[mid] > key) {
                upper = mid;
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }
        return upper;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        HITeam = new int[N];
        ARCTeam = new int[M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            HITeam[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            ARCTeam[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(ARCTeam);            

        long winCnt = 0;                 
        long loseCnt = 0;                 
        long tieCnt = 0;                  

        for (int member : HITeam) {
            int lower = lowerBound(ARCTeam, member);      
            int upper = upperBound(ARCTeam, member);      
            int equal = upper - lower;                    
            int greater = M - upper;                       

            winCnt += lower;
            tieCnt   += equal;
            loseCnt += greater;
        }

        System.out.println(winCnt + " " + loseCnt + " " + tieCnt);
    }
}
