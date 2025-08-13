import sys

sys.setrecursionlimit(10 ** 6)


class TreeNode:
    def __init__(self, val=[], left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode[val: {self.val}, left: {self.left}, right: {self.right}]"


def solution(nodeinfo):  # x, y니까 유의하자.
    def bst(nodeinfo):
        if not nodeinfo:
            return None

        sorted_nodeinfo = sorted(nodeinfo, key=lambda node: (-node[1], node[0]))
        max_y_node = sorted_nodeinfo[0]
        idx = nodeinfo.index(max_y_node)

        node = TreeNode(max_y_node)
        node.left = bst(nodeinfo[:idx])
        node.right = bst(nodeinfo[idx + 1:])
        return node

    def front_search(node):
        if node:
            front_result.append(node_number_dic[node.val])
            front_search(node.left)
            front_search(node.right)
        return

    def back_search(node):
        if node:
            back_search(node.left)
            back_search(node.right)
            back_result.append(node_number_dic[node.val])
        return

    nodeinfo = list(map(tuple, nodeinfo))

    node_number_dic = {node: i for i, node in enumerate(nodeinfo, start=1)}

    node = bst(sorted(nodeinfo))

    # 자 이제 node을 탐색하자.
    front_result = []
    back_result = []
    front_search(node)
    back_search(node)

    answer = [front_result, back_result]
    return answer


import sys

sys.setrecursionlimit(10000)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


# 이 문제의 생각의 방향은 루트노드를 구해야한다는 것이었고
# 그리고 루트노드의 왼편은 모두 x값이 작은 것 오른편은 x값이 큰것이라는 기본 개념을 구현하면 되었다.
def solution2(nodeinfo):  # x, y니까 유의하자.
    def to_binary_serch_tree(nodeinfo):
        if not nodeinfo:
            return None

        # nodeinfo.sort(key=lambda node: (-node[1]))
        root = nodeinfo[0]
        left = to_binary_serch_tree([node for node in nodeinfo if node[0] < root[0]])
        right = to_binary_serch_tree([node for node in nodeinfo if node[0] > root[0]])
        return TreeNode(root, left, right)

    def preorder(treenode):
        if not treenode:
            return
        result1.append(nodeinfo_dic[tuple(treenode.val)])
        preorder(treenode.left)
        preorder(treenode.right)

    def postorder(treenode):
        if not treenode:
            return
        postorder(treenode.left)
        postorder(treenode.right)
        result2.append(nodeinfo_dic[tuple(treenode.val)])

    nodeinfo_dic = {tuple(node): idx + 1 for idx, node in enumerate(nodeinfo)}
    nodeinfo.sort(key=lambda node: (-node[1]))
    treenode = to_binary_serch_tree(nodeinfo)
    result1, result2 = [], []
    preorder(treenode)
    postorder(treenode)
    return [result1, result2]



