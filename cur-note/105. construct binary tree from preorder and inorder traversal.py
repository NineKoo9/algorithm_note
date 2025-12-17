# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 순서가 주어지니까 이제 트리를 만들어야한다.
        # 전위순회의 첫번째 녀석이 중위순회의 반을 가른다. 이것을 가지고 구축해보자.
        if not (preorder and preorder[0] in inorder):
            return 
        # 이제 루트노드를 구축한다.
        # 사용한 루트는 제거한다.
        first = preorder.pop(0)
        inorder_mid_idx = inorder.index(first)
        treenode = TreeNode(first)
        treenode.left = self.buildTree(preorder, inorder[:inorder_mid_idx])
        treenode.right = self.buildTree(preorder, inorder[inorder_mid_idx:])
        return treenode