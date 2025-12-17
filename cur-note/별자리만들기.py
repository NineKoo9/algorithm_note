import math


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


    def get_dist(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2,), 2)

    n = int(input())
    graph = [tuple(map(float, input().split())) for _ in range(n)]
    graph_with_dist = []
    for i in range(n):
        for j in range(i + 1, n):
            node1 = graph[i]
            node2 = graph[j]
            dist = get_dist(node1, node2)
            graph_with_dist.append((i, j, dist))

    graph_with_dist.sort(key=lambda line:line[2])
    parent_table = [i for i in range(n)]
    min_dist = 0
    for n1, n2, dist in graph_with_dist:
        if union(n1, n2):
            min_dist += dist
    print(min_dist)

def solution3():
    import math

    def find_parent(node):
        if node == parent_table[node]:
            return node
        parent_table[node] = find_parent(parent_table[node])
        return parent_table[node]

    def union(node_a, node_b):  # 어짜피 node_1, node_2 는 연결되어 있고... 연결하지 못하는 경우는 이미 연결된 경우구나
        parent_a = find_parent(node_a)
        parent_b = find_parent(node_b)
        if parent_a == parent_b:
            return False
        if parent_a < parent_b:
            parent_table[parent_b] = parent_a  # 이야... 여기서 헷갈렸네... parent_table[node_b] 이렇게 되어 있으면... 부모가 연결이 안되어 버리지...
        else:
            parent_table[parent_a] = parent_b
        return True

    def get_distance(node1: tuple, node2: tuple) -> float:
        x1, y1 = node1
        x2, y2 = node2
        return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

    n = int(input())
    star_points = [tuple(map(float, input().split())) for _ in range(n)]

    # 어쨋든 모든 거리를 다 구해보자
    lines_with_dist = []
    for star1 in range(n):
        for star2 in range(star1 + 1, n):
            star1_point = star_points[star1]
            star2_point = star_points[star2]
            lines_with_dist.append((star1, star2, get_distance(star1_point, star2_point)))

    lines_with_dist.sort(key=lambda line:line[2])
    parent_table = [i for i in range(n)]
    cost = 0
    for node1, node2, dist in lines_with_dist:
        if union(node1, node2):
            cost += dist
    print(cost)


def solution4():
    from itertools import combinations
    import math

    def calc_dist(a, b):
        return round(math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)), 2)

    def find_parend(node):
        if node == parent[node]:
            return node
        parent[node] = find_parend(parent[node])
        return parent[node]

    def union(a, b):
        pa = find_parend(a)
        pb = find_parend(b)
        if pa == pb:
            return False
        else:
            if pa > pb:
                parent[pa] = pb
            else:
                parent[pb] = pa
            return True

    n = int(input())
    stars = [list(map(float, input().split())) for _ in range(n)]

    star_pair = [(calc_dist(stars[idx1], stars[idx2]), idx1, idx2) for idx1, idx2 in combinations(range(n), 2)]
    star_pair.sort()

    parent = [i for i in range(n)]
    total_cost = 0
    for cost, star1, star2 in star_pair:
        # 비용이 낮은 순서로 계속 집합에 추가해나간다.
        if union(star1, star2):
            total_cost += cost
    print(total_cost)


solution4()


# 모든 거리를 구하는 것 4950 밖에 안하니까 할만하다.