def solution():
    def find_parent(node):
        if node == parent_table[node]:
            return node
        parent_table[node] = find_parent(parent_table[node])
        return parent_table[node]

    def union(node1, node2):
        p1 = find_parent(node1)
        p2 = find_parent(node2)
        if p1 == p2:
            return False
        else:
            if p1 > p2:
                parent_table[p1] = p2
            else:
                parent_table[p2] = p1
            return True


    V, E = map(int, input().split())
    lines = [tuple(map(int, input().split())) for _ in range(E)]
    lines.sort(key=lambda line: line[2])
    parent_table = [i for i in range(V + 1)]
    total_cost = 0
    for n1, n2, cost in lines:
        if union(n1, n2):
            total_cost += cost
    print(total_cost)


def solution2():
    import sys

    sys.setrecursionlimit(100000)
    def find_parent(node):
        if parent_table[node] == node:
            return node
        parent_table[node] = find_parent(parent_table[node])
        return parent_table[node]

    def union(node1, node2):
        p1 = find_parent(node1)
        p2 = find_parent(node2)
        if p1 == p2:
            return False
        if p1 > p2:
            parent_table[p1] = p2
        else:
            parent_table[p2] = p1
        return True


    V, E = map(int, input().split())
    graph_info = [list(map(int, input().split())) for _ in range(E)]

    parent_table = [i for i in range(V)]

    graph_info.sort(key=lambda info: info[2])

    result = 0
    for node1, node2, cost in graph_info:
        if union(node1 - 1, node2 - 1):
            result += cost

    print(result)

solution2()