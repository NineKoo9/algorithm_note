import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 분할 정복 방식으로 전위 순회를 찾음
def preorder(in_start, in_end, post_start, post_end):
    # 재귀 종료 조건 (수렴)
    if(in_start > in_end) or (post_start > post_end):
        return

    # 후위 순회 결과의 끝이 (서브)트리의 루트임을 이용
    parents = postorder[post_end]
    print(parents, end=" ")

    # 중위 순회에서 루트의 좌 우로 자식들이 갈라지는 것을 이용하여 left, right를 선언
    left = position[parents] - in_start
    right = in_end - position[parents]

    # left, right로 나눠 분할 정복 방식으로 트리를 추적하여 전위 순회를 찾아냄
    preorder(in_start, in_start+left-1, post_start, post_start+left-1) # 쪽 서브트리
    preorder(in_end-right+1, in_end, post_end-right, post_end-1) # 오른쪽 서브트리

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 후위 순회의 끝값이 중위 순회의 어디 인덱스에 위치한지 확인을 위해
# 중위 순회의 값들의 인덱스값을 저장
position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i

# 중위 순회, 후위 순회 모두 0부터 n-1 (전체 범위)값을 주고 전위 순회를 구함
preorder(0, n-1, 0, n-1)

# 아래의 코드는 메모리초과가 나타난다.
# class TreeNode:
#     def __init__(self, val = 0, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#     def __str__(self):
#         return f"TreeNode[val={self.val}, left={self.left}, right={self.right}]"
#
# def solution2():
#     # 인오더와 포스트 오더가 주어진다면... 어떻게 하지?
#     # 포스터 오더는 left, right, root순으로 순회한다.
#     # 그렇다면 postorder의 마지막은 인오더에서 루트를 나누게 될 것이다.
#     def to_binary_tree(inorder, postorder):
#         if not inorder:
#             return None
#
#         idx = inorder.index(postorder.pop())
#         node = TreeNode(inorder[idx])
#         node.right = to_binary_tree(inorder[idx + 1:], postorder)
#         node.left = to_binary_tree(inorder[:idx], postorder)
#         return node
#
#     def preorder(node):
#         if not node:
#             return None
#
#         result.append(node.val)
#         preorder(node.left)
#         preorder(node.right)
#
#     n = int(input())
#     inorder = list(map(int, input().split()))
#     postorder = list(map(int, input().split()))
#     binary_tree = to_binary_tree(inorder, postorder)
#
#     result = []
#     preorder(binary_tree)
#     print(*result)
#
# solution2()