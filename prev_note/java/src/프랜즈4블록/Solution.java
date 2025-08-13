package 프랜즈4블록;

import java.util.*;

class Solution {
    public int solution(int m, int n, String[] b) {
        char[][] board = new char[b.length][];
        for (int i = 0; i < b.length; i++) {
            board[i] = b[i].toCharArray();
        }
        while (true) {
            int[][] removeNum = getRemoveNum(board);
            if (removeNum.length == 0) {
                break;
            }
            board = boardUpdate(board, removeNum);
        }
        int count = 0;
        for (char[] row : board) {
            for (int i = 0; i < row.length; i++) {
                if (row[i] == '0') {
                    count++;
                }
            }
        }
        return count;
    }

    public char[][] boardUpdate(char[][] board, int[][] points) {
        Stack<Character> stack = new Stack<>();
        for (int[] point : points) {
            board[point[0]][point[1]] = '0';
        }
        for (int j = 0; j < board[0].length; j++) {
            for (int i = 0; i < board.length; i++) {
                if (board[i][j] != '0') {
                    stack.add(board[i][j]);
                }
            }
            for (int i = board.length - 1; i >= 0; i--) {
                board[i][j] = !stack.isEmpty() ? stack.pop() : '0';
            }
        }
        return board;
    }

    public int[][] getRemoveNum(char[][] board) {
        Set<int[]> answer = new HashSet<>();
        for (int i = 0; i < board.length - 1; i++) {
            for (int j = 0; j < board[0].length - 1; j++) {
                if (board[i][j] == '0') {
                    continue;
                }
                if (board[i][j] == board[i + 1][j]
                        && board[i][j] == board[i][j + 1]
                        && board[i][j] == board[i + 1][j + 1]) {
                    answer.add(new int[]{i, j});
                    answer.add(new int[]{i + 1, j});
                    answer.add(new int[]{i, j + 1});
                    answer.add(new int[]{i + 1, j + 1});
                }
            }
        }
        return answer.toArray(new int[answer.size()][]);
    }
}

class main{
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(4, 5, new String[]{"CCBDE", "AAADE", "AAABF", "CCBBF"}));
    }
}