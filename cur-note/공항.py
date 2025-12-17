def solution():
    def find_parent(node):
        if node == parent_table[node]:
            return node
        parent_table[node] = find_parent(parent_table[node])
        return parent_table[node]

    def union(a, b):
        p_a = find_parent(a)
        p_b = find_parent(b)
        if p_a > p_b:
            parent_table[p_a] = p_b
        else:
            parent_table[p_b] = p_a


    G = int(input())  # 게이트의 수
    P = int(input())  # 비행기의 수 둘다 각각 최대 10만까지 가능하다.
    available_gates = [int(input()) for _ in range(P)]  # g_i값은 i번째 비행기가 0 ~ i번째에 파킹이 가능하다.

    parent_table = [i for i in range(G + 1)]

    # 여기서 union_find알고리즘을 생각한다는 것... parent을 두고.. 그보다 앞인
    ans = 0
    for max_gate in available_gates:
        parent = find_parent(max_gate)
        if parent == 0:
            break
        union(parent, parent - 1)
        ans += 1

    print(ans)

solution()