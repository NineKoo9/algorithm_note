import sys

def solution():
    sys.setrecursionlimit(100000)
    input = sys.stdin.readline
    def dfs(node):
        if not graph[node]:
            return delay_times[node]

        if dp[node] != -1:
            return dp[node]

        # 여기서 그리디하게 가는 것을 어떻게 하지...?
        max_time = -1
        for n_node in graph[node]:
            max_time = max(max_time, dfs(n_node))
        dp[node] = max_time + delay_times[node]

        return dp[node]

    T = int(input())

    for _ in range(T):
        # 건물의 갯수 N, 건설 순서 규칙 K개
        N, K = map(int, input().split())

        delay_times = list(map(int, input().split()))

        # 순서는 x가 지어져야 y가 지어진다. 이것을 y에서 x로 갈 수 있다로 정한다.
        graph = [[] for _ in range(N)]
        construct_roles = [list(map(lambda s: int(s) - 1, input().split())) for _ in range(K)]
        for a, b in construct_roles:
            graph[b].append(a)

        start = int(input()) - 1
        dp = [-1] * N  # 여기서 0000으로 초기화하면 왜 시간초과가 나타나는 것이지...?
        print(dfs(start))  # dfs가 무슨 역할을 할지 너가 명확히 정하지 못했어. 그러니까 어떤 값을 반환하는 함수일지.. 막연히 탐색해야겠다고만 생각했어.

def solution2():
    def dfs(node):
        if not graph[node]:
            dp[node] = construction_time[node]
            return construction_time[node]

        if dp[node] != -1:
            return dp[node]

        # dp초기화를 어디서 해야할지 고민이네...
        # 초기화를 하고 반환한다고 하면.. 딱 일관된거 같다.
        max_time = 0
        for n_node in graph[node]:
            max_time = max(max_time, dfs(n_node))
        dp[node] = max_time + construction_time[node]
        return dp[node]

    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        construction_time = list(map(int, input().split()))
        priorities = [list(map(lambda num: int(num) - 1, input().split())) for _ in range(K)]
        dest = int(input()) - 1

        graph = [[] for _ in range(N)]
        for a, b in priorities:
            graph[b].append(a) # b가 지어지기 위해서는 a가 지어져야함.

        dp = [-1] * N
        print(dfs(dest))



solution2()