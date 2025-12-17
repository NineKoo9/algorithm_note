from collections import deque
import sys

sys.setrecursionlimit(100000)
def solution():
    def get_max_node(node, dist):
        max_node = node
        max_dist = dist

        for n_node, n_dist in graph[node]:
            if visited[n_node]:
                continue
            visited[node] = 1
            n, d = get_max_node(n_node, dist + n_dist)
            if d > max_dist:
                max_node = n
                max_dist = d

        return max_node, max_dist

    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        parent, child, cost = map(int, input().split())
        graph[parent].append((child, cost))
        graph[child].append((parent, cost))

    # 임의의 한점에서 가장 먼 점은 어떻게 구할까?
    start = 1
    visited = [0] * (N + 1)
    node, dist = get_max_node(start, 0)

    # 그렇다면 이제 node에서 가장 먼 거리를 찾으면 되겠다!
    visited = [0] * (N + 1) # 하... 이걸 다시 초기화를 안했네...
    answer_node, answer_dist = get_max_node(node, 0)
    print(answer_dist if start != answer_node else dist)

# 아... 이건 내가 이진트리라 가정해서 틀린 풀이...!
def solution2():
    import sys

    sys.setrecursionlimit(100000)

    tree_max_len = 0

    def dfs(node):
        nonlocal tree_max_len
        
        if not node:
            return 0

        left_node, left_length = None, 0
        right_node, right_length = None, 0

        if graph[node] :
            left_node, left_length = graph[node][0]
        if len(graph[node]) > 1 :
            right_node, right_length = graph[node][1]

        left_max_length = dfs(left_node) + left_length
        right_max_length = dfs(right_node) + right_length

        tree_max_len = max(tree_max_len, left_max_length + right_max_length)

        print(f"{node}노드에서 가장 긴 길이는 {left_max_length + right_max_length} 이다.")
        return max(left_max_length, right_max_length)

    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n - 1)]

    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for p_node, c_node, length in lines:
        graph[p_node].append((c_node, length))

    dfs(1)
    print(tree_max_len)


# 위의 이진트리로 처리한 코드를 정리한 것임
def solution_clean():
    input = sys.stdin.readline
    
    # ... 입력 부분은 동일 ...
    try:
        line = input()
        if not line: return
        n = int(line)
        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            p, c, w = map(int, input().split())
            graph[p].append((c, w))
    except ValueError: return

    tree_max_len = 0

    def dfs(node):
        nonlocal tree_max_len
        
        # 1. [핵심] 리스트 컴프리헨션으로 자식들의 깊이를 한 방에 계산
        # 자식이 없으면 빈 리스트 []가 됩니다.
        depths = [dfs(child) + weight for child, weight in graph[node]]
        
        # 2. [핵심] 0을 두 개 채워 넣습니다 (Padding)
        # 자식이 0명 -> [0, 0]
        # 자식이 1명(길이 10) -> [10, 0, 0]
        # 자식이 2명(길이 10, 5) -> [10, 5, 0, 0]
        depths.extend([0, 0])
        
        # 3. 정렬 후 상위 2개만 취하면 끝!
        # if len(...) 같은 체크가 전혀 필요 없습니다.
        depths.sort(reverse=True)
        
        # 가장 긴 두 개의 합으로 지름 갱신
        tree_max_len = max(tree_max_len, depths[0] + depths[1])
        
        # 가장 긴 줄기 하나 리턴
        return depths[0]

    dfs(1)
    print(tree_max_len)

def solution3():
    import sys

    sys.setrecursionlimit(100000)

    # 가장 먼 노드를 찾아야한다.
    def dfs(cur_node):
        deepest_node, deepest_len = cur_node, 0
        for n_node, n_len in graph[cur_node]:
            if visited[n_node]:
                continue
            visited[n_node] = 1
            leaf_deepest_node, leaf_deepest_len = dfs(n_node)
            visited[n_node] = 0
            if deepest_len < n_len + leaf_deepest_len:
                deepest_len = n_len + leaf_deepest_len
                deepest_node = leaf_deepest_node
        return deepest_node, deepest_len

    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n - 1)]

    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for p_node, c_node, length in lines:
        graph[p_node].append((c_node, length))
        graph[c_node].append((p_node, length))

    visited = [0 for _ in range(n + 1)]

    visited[1] = 1
    deepest_node, _ = dfs(1)
    visited[1] = 0

    visited[deepest_node] = 1
    tree_max_len = dfs(deepest_node)[1]
    print(tree_max_len)

solution3()