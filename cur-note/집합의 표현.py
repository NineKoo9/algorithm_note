import sys

sys.setrecursionlimit(10000)

def solution():
    def find_parent(node):
        if node == parent_table[node]:
            return node
        parent_table[node] = find_parent(parent_table[node])
        return parent_table[node]

    def union(node1, node2):
        p1 = find_parent(node1)
        p2 = find_parent(node2)
        if p1 <= p2:
            parent_table[p2] = p1
        else:
            parent_table[p1] = p2

    n, m = map(int, input().split())
    operations = [tuple(map(int, input().split())) for _ in range(m)]
    parent_table = [i for i in range(n + 1)]
    for operate, node1, node2 in operations:
        if operate == 1:
            p1 = find_parent(node1)
            p2 = find_parent(node2)
            if p1 == p2:
                print("YES")
            else:
                print("NO")
        else:
            union(node1, node2)

solution()