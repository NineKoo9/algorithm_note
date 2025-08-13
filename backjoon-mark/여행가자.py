def solution():
    def find_parent(node):
        if node == parent_table[node]:
            return node
        parent_table[node] = find_parent(parent_table[node])
        return parent_table[node]

    def union(node1, node2):
        p1 = find_parent(node1)
        p2 = find_parent(node2)
        if p1 >= p2:
            parent_table[p1] = p2
        else:
            parent_table[p2] = p1

    N = int(input())
    M = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    parent_table = [i for i in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                union(i, j)


    schedule_node_lst = list(map(lambda node: int(node) - 1, input().split()))
    p = find_parent(schedule_node_lst[0])
    for s_node in schedule_node_lst:
        if p != find_parent(s_node):
            print("NO")
            e
    print("YES")



solution()