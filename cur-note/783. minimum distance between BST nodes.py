# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    ans = 100000
    prev = -100000

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # 이 문제가 중위순회라는 것을 어떻게 인지할까?
        # 정렬이 되어있을때 인접한 녀석들을 탐색하면 가장 작은 차이를 구할 수 있다.
        # 그렇다면 중위순회를 하며 인접한 녀석들을 탐색하면 되겠다. 그러면서 현재 노드와 앞 녀석을 비교하면 될듯
        if root.left:
            self.minDiffInBST(root.left)

        current_val = root.val
        
        self.ans = min(self.ans, current_val - self.prev)
        self.prev = current_val # 이전에 탐색했던 값을 담아갈 것이다.
        
        if root.right:
            self.minDiffInBST(root.right)
        
        return self.ans



        
        