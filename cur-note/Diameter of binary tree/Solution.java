
// Definition for a binary tree node.
import java.util.*;


class Solution {
    static int maxLength;

    public int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftDist = dfs(node.left);
        int rightDist = dfs(node.right);
        maxLength = Math.max(maxLength, leftDist + rightDist);
        return Math.max(leftDist, rightDist) + 1;
    }

    public int diameterOfBinaryTree(TreeNode root) {
        maxLength = 0;
        dfs(root);
        return maxLength;
    }

    static class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
     }
}
}