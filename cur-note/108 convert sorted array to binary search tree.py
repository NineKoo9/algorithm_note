# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 정렬된 배열을... bst로 만들어야한다.
        # 이것을 어케할까?
        if not nums:
            return

        mid_idx = len(nums) // 2
        node = TreeNode()
        node.left = self.sortedArrayToBST(nums[:mid_idx])
        node.right = self.sortedArrayToBST(nums[mid_idx + 1:])
        node.val = nums[mid_idx]
        
        return node