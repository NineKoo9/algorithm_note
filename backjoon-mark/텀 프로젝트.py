import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    call_stack.append(start)
    friend = selected_friends[start]

    # 방문한 적이 있고 콜스택 안에 있다면 그 녀석 이후의 녀석들은 모두 같은 사이클일 수 있다.
    # 이 부분이 진짜 어렵네
    if visited[friend]:
        if friend in call_stack:
            for i in call_stack[call_stack.index(friend):]:
                cycle[i] = True
        return
    else:
        dfs(friend)

for _ in range(int(input())):
    n = int(input())
    selected_friends = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(n + 1)]

    # 사이클을 이룬 학생
    cycle = [False] * (n + 1)
    for now in range(1, n + 1):
        if not visited[now]:
            call_stack = []
            dfs(now)
    print(cycle.count(False) - 1)