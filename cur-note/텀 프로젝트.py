from itertools import cycle


def solution1():
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

# 확실한 것은 한 노드에서 다른 한 노드로 향하는 방향은 하나라는 것이다.
# 이 풀이는 풀다가 말았던 풀이라 올바르지 않음.
def solution2():
    def dfs(node):
        # 방문 처리를 하였고
        # 현재의 길에 포함된다.
        visited[node] = True
        path.append(node)

        # 이건 그냥 하나 아니면 0개 일 것이다.
        for n_node in graph[node]:
            # 자 여기서 다음 노드를 탐색하는데...
            if visited[n_node]:
                if n_node in path:
                    while True:
                        prev_node = path.pop()
                        is_cycle[prev_node] = True
                        if prev_node == node:
                            break
                else:
                    break
            # 방문한 적이 없다면?
            dfs(n_node)
        # 이제남아있는path는 모두 cycle을 이루지 않는다.
        while path:
            node = path.pop()
            is_cycle[node] = False

    T = int(input())
    for i in range(T):
        n = int(input())
        selected_friends = [0] + list(map(int, input().split()))

        # 일단 그래프를 초기화하자.
        graph = [[] for _ in range(n + 1)]
        for a, b in enumerate(selected_friends[1:], start=1):
            graph[a].append(b)

        # 일단 생각해보자. dfs을 통해서 탐색해 나가다보니 현재의 탐색경로에서
        # 똑같은 점으로 도달할 수 있다. 그렇다면 그 녀석 이후의 모든 점들은
        # 사이클안에 있다고 할 수 있다. 그리고 경로상에 있던 점들은 모두 체크를하였고
        # 사이클 밖에 있던 점들은 사이클을 이루지 않는다고 생각해도 될 것이다?
        visited = [False for _ in range(n + 1)]
        path = []
        is_cycle = [False for _ in range(n + 1)]
        for now in range(1, n + 1):
            dfs(now)


def solution3():
    def dfs(node: int):
        visited[node] = True
        path = [node]
        path_dict = {node: 0} # 조금 더 속도를 빠르게 하기 위함.

        # 어짜피 노드는 하나이겠지만... 존재하는지 안하는지 if문을 생략해도 되니 이걸 사용하자.
        while 1:
            next_node = selected_friends[node]
            if next_node in path_dict:
                visited[next_node] = True
                start_idx = path_dict[next_node]
                while len(path) > start_idx:
                    prev_node = path.pop()
                    is_cycle[prev_node] = True
                break
            # pass에 속한 녀석이 아니고, 방문한 녀석이라면? 이미 cycle여부가 결정되었을 것이고
            # 더 탐색할 필요는 없다. -> 현재 path에 남아있는 녀석들은 모드 사이클아님
            if visited[next_node]:
                break

            # 방문한적도 없고 현재의 path에 속하지도 않았다면?
            visited[next_node] = True
            path.append(next_node)
            path_dict[next_node] = path_dict[node] + 1
            node = next_node

        for remained_node in path:
            is_cycle[remained_node] = False

    T = int(input())
    for i in range(T):
        n = int(input())
        input_lst = list(map(int, input().split()))
        selected_friends: dict[int, int] = {a: b for a, b in enumerate(input_lst, start = 1)}
        visited = [False for _ in range(n + 1)]
        is_cycle = [False for _ in range(n + 1)]

        # now 부터 탐색한다.
        for now in range(1, n + 1):
            if visited[now]:
                continue
            dfs(now)
        print(n - sum(is_cycle))

solution3()

# solution3에서 dict을 안쓰고 그냥해보니까 시간초과가 걸리네?
# solution1()에 비해서 어떤 부분이 병목일까?
# solution1은 visited로 가지치기를 적절하게 해주기때문에 병목이 안생김. 하지만 solution4는 매번 새로운 노드마다 in 연산으로 확인하기 때문에 시간복잡도ㅗ가 엄청나게 올라감.
def solution4():
    def dfs(node: int):
        visited[node] = True
        path = [node]

        while 1:
            next_node = selected_friends[node]
            if next_node in path:
                visited[next_node] = True
                start_idx = path.index(next_node)
                while len(path) > start_idx:
                    prev_node = path.pop()
                    is_cycle[prev_node] = True
                break
            # pass에 속한 녀석이 아니고, 방문한 녀석이라면? 이미 cycle여부가 결정되었을 것이고
            # 더 탐색할 필요는 없다. -> 현재 path에 남아있는 녀석들은 모드 사이클아님
            if visited[next_node]:
                break

            # 방문한적도 없고 현재의 path에 속하지도 않았다면?
            visited[next_node] = True
            path.append(next_node)
            node = next_node

        for remained_node in path:
            is_cycle[remained_node] = False

    T = int(input())
    for i in range(T):
        n = int(input())
        input_lst = list(map(int, input().split()))
        selected_friends: dict[int, int] = {a: b for a, b in enumerate(input_lst, start = 1)}
        visited = [False for _ in range(n + 1)]
        is_cycle = [False for _ in range(n + 1)]

        # now 부터 탐색한다.
        for now in range(1, n + 1):
            if visited[now]:
                continue
            dfs(now)
        print(n - sum(is_cycle))

solution4()