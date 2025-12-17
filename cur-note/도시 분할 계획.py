def solution():
    def union(node1, node2):
        node1_p, node2_p = find_parent(node1), find_parent(node2)
        if node1_p == node2_p:
            return False
        elif node1_p < node2_p:
            parent_table[node2_p] = node1_p
        else:
            parent_table[node1_p] = node2_p
        return True

    def find_parent(node):
        if node == parent_table[node]:
            return node
        parent_table[node] = find_parent(parent_table[node])
        return parent_table[node]

    N, M = map(int, input().split())
    road_info_lst = [tuple(map(int, input().split())) for _ in range(M)]
    road_info_lst.sort(key=lambda road_info: road_info[2])

    parent_table = [i for i in range(N + 1)]
    divide_count = N
    min_cost = 0
    if N == 2:
        print(0)
        exit()
    for a_house, b_house, cost in road_info_lst:
        if union(a_house, b_house):
            divide_count -= 1
            min_cost += cost
            if divide_count == 2:
                break
    print(min_cost)

solution()