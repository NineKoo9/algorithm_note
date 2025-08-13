def solution():  # 현재 이 풀이는 50만개가 모두 같은 경우 엄청난 시간복잡도를 가지게 된다. 50만명이 모두 서로를 볼 수 있는데...
    N = int(input())
    person_heights = [int(input()) for _ in range(N)]
    stack = []
    count = 0
    for height in person_heights:
        temp = stack.copy()
        # 현재 높이에서 서로 볼 수 있는 녀석들을 세어본다.
        while temp:
            # 현재의 높이에서 스택안에 있는 녀석의 높이가 더 크다면 그 다음 녀석들은 볼것도 없이 쌍을 이룰 수 없다.
            if temp[-1] > height:
                count += 1
                break
            else:  # temp[-1] < height
                count += 1
            temp.pop()
        # 스택은 내림차순으로 쌓아간다. 어짜피 본인보다 작은 녀석이 아래에 있으면 쌍을 맺을 수 없다. 근데 생각해 보니 같은 녀석도 맺을 수 없는데...
        # 근데 이것도 확인하는 녀석이 아래에 있는 경우다. 확인하는 녀석이 더 높다면? 모두 쌍을 맺을 수 있다.
        while stack and stack[-1] < height:
            stack.pop()
        stack.append(height)

    print(count)

def solution2():  # 생각해보니 위의 풀이는... 계속해서 stack 의 탐색이 중복된다. 설계자체가 잘못된 것 같다.
    N = int(input())
    person_heights = [int(input()) for _ in range(N)]
    stack = []
    count = 0
    for height in person_heights:
        num = 1
        while stack and stack[-1][0] <= height:
            if stack[-1][0] == height:
                count += stack[-1][1]  # 현재녀석이 B인 경우에서 쌍의 수를 구한다.
                num = stack[-1][1] + 1 # 현재 녀석을 갯수에 포함시킨다.
                stack.pop()
            else:  # stack[-1][0] < height
                count += stack[-1][1]
                stack.pop()
                num = 1
        # height 가 더 작다면? 가능한 케이스는 인접한 녀석 딱 하나밖에 없지.
        if stack:  # 여기서 당연히 if stack and stack[-1] > height
            count += 1
        stack.append((height, num))

    print(count)


def solution3():
    N = int(input())
    person_heights = [int(input()) for _ in range(N)]

    stack = []
    visible_pairs = 0

    for height in person_heights:
        count_same_height = 1  # 바로 현재의 height에서 바라볼 수 있는 녀석들을 카운트하니까 마지막에 stack에 남아있어도 문제가 없군

        # 스택의 마지막 사람보다 현재 키가 크거나 같을 때 처리
        while stack and stack[-1][0] <= height:
            # 이 부분은 현재의 height에서 볼수있는 녀석들을 체크해 나가는 부분이다.
            prev_height, prev_count = stack.pop()
            visible_pairs += prev_count

            # 같은 키라면 같은 그룹으로 묶어 처리
            if prev_height == height:
                count_same_height += prev_count

        # 스택이 비어있지 않다면, 현재 사람은 이전 사람을 볼 수 있음
        if stack:  # 정확히는 stack and stack[-1][0] > height
            visible_pairs += 1

        # 현재 사람의 키와 같은 그룹의 수를 스택에 추가
        stack.append((height, count_same_height))

    print(visible_pairs)

# 이분탐색을 넣었는데 시간초과가 걸렸다.
# 기본적으로 최악인 50만 * log(50)
def solution4():
    from bisect import bisect_right
    from collections import deque
    import sys
    def my_bisect_right(lst, num):
        # 나는 이분탐색을 이용해서.. 감소하는 lst에서 num이 들어갈 위치를 찾는다.
        s = 0
        e = len(lst) - 1
        while s + 1 < e:
            mid = (s + e) // 2
            if lst[mid] > num:
                s = mid
            else:
                e = mid
        return s

    print(my_bisect_right([6, 5, 4, 4, 4, 3, 2, 1], 3))
    print(my_bisect_right([6, 5, 4, 4, 4, 3, 2, 1], 4))
    print(my_bisect_right([6, 5, 4, 4, 4, 3, 2, 1], 5))
    print(my_bisect_right([6, 5, 4, 4, 4, 3, 2, 1], 7))


    input = sys.stdin.readline

    N: int = int(input())

    # 키는 서있는 순서대로 주어진다.
    heights: list[int] = [int(input()) for _ in range(N)]

    q: deque = deque()  # 이것은 하향하는 스택이다.
    answer: int = 0
    for b_height in heights:
        # 먼저 볼 수 있는 녀석들의 갯수를 구한다.
        if q:
            idx = bisect_right(q, b_height)
            answer += (idx + 1) if idx < len(q) else idx

        # q는 우상향하도록 만든다.
        while q and q[0] < b_height:
            q.popleft()
        q.appendleft(b_height)

    print(answer)


def solution5():
    import sys
    input = sys.stdin.readline

    def my_bisect(lst, num):
        # 나는 이분탐색을 이용해서.. 감소하는 lst에서 num이 들어갈 위치를 찾는다.
        s = 0
        e = len(lst)
        while s + 1 < e:
            mid = (s + e) // 2
            if lst[mid] > num:
                s = mid
            else:
                e = mid
        return s

    N: int = int(input())

    # 키는 서있는 순서대로 주어진다.
    heights: list[int] = [int(input()) for _ in range(N)]

    stack = []  # 이것은 하향하는 스택이다.
    answer = 0
    for b_height in heights:
        # 먼저 볼 수 있는 녀석들의 갯수를 구한다.
        if stack:
            idx = my_bisect(stack, b_height)
            answer += len(stack) - idx

        # q는 우상향하도록 만든다.
        while stack and stack[-1] < b_height:
            stack.pop()
        stack.append(b_height)

    print(answer)

solution5()
# 13 8877766777799 이 상황에서 틀린다.
# 어떤 예외상황이 발생할 수 있을까?
# stack 안에 있는 녀석들은 모두 쌍을 만들 수 있는거 아닐까
# 아 a 또는 b 보다 큰 녀석이 없어야 한다는 것이다. 그러니까... b를 비교할때 스택안에 큰 녀석들이 여럿 잇으면 안되겠네...
# 단순히 스택에서 작거나 같은 녀석으로 쌓아가는 것은 문제가 된다. 특히 두번째 연산수가 Stack 제일 위에 있는 녀석보다 작다면 더 문제다.