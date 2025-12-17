import sys
sys.setrecursionlimit(10000)

class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"TreeNode[val: {self.val}, left: {self.left}, right: {self.right}]"
        
        

def preorder(tree, path):
    if not tree:
        return 
    
    path.append(tree.val)
    preorder(tree.left, path)
    preorder(tree.right, path)
    return path

def postorder(tree, path):
    if not tree:
        return
    
    postorder(tree.left, path)
    postorder(tree.right, path)
    path.append(tree.val)
    return path

def solution(nodeinfo):
    from collections import deque
    
    def to_bst(x_info):
        if not x_info:
            return 
        
        root_point = max(x_info, key=lambda node: node[1])
        root_point_idx = x_info.index(root_point)
        left = to_bst(x_info[:root_point_idx])
        right = to_bst(x_info[root_point_idx + 1:])
        
        root_val = node_val_dict[root_point]
        return TreeNode(root_val, left, right)
        
    nodeinfo = list(map(tuple, nodeinfo))
    node_val_dict = {node: idx for idx, node in enumerate(nodeinfo, start = 1)}
    treenode = to_bst(sorted(nodeinfo, key = lambda node: (node[0], -node[1])))
    # 이제 treenode을 전위 후위 순회를 하면 된다.
    result1 = preorder(treenode, [])
    result2 = postorder(treenode, [])
    
    return [result1, result2]