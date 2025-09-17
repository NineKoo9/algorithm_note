# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = 0

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 흠... 보니까 역순으로 더해나가는 것이구나?
        # 중위순회를 역순으로 하면 될듯?
        # 근데 다시 이것을 트리로 만들어야한다.
        # 어쨋든 이전 값을 계속 기록해나가야한다.
        if not root:
            return
        right = self.bstToGst(root.right)
        val = root.val + self.prev
        self.prev = val
        left = self.bstToGst(root.left)
        return TreeNode(val, left, right)

        