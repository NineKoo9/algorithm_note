
# 이 풀이는 연속된 집합을 먼저 찾는 것부터 잘못되었다. 적어도 K개 라는 부분을 최적화 하지 못했기에
# 나는 그림으로 그릴때 이미 정렬된 상태로 연속적인 경우를 상정했다. 하지만... 장렬된 상태가 아니라면 연속적인 것을 아무런 의미가 없다.
#
def solution():
    N = int(input())  # 50보다 같거나 작다.
    checkers = [list(map(int, input().split())) for _ in range(N)]

    answer = [0]
    for k in range(1, N):
        # 이제부터 k번째 수(0부터 시작)에는 적어도 k + 1개의 체커가 모이는 가장 작은 수를 구하는 것이다.
        # 그렇다면 길이가 n인 연속적인 경우의 수를 살펴보자.
        min_total_cost = int(1e9)
        for i in range(N - k):
            j = i + k  # i와 j는 시작과 끝의 인덱스이다.

            # 그렇다면 이 사이에서 최소의 이동 거리를 구해야하는데
            temp_checkers = checkers[i:j + 1]
            temp_len = k + 1

            # temp_checkers의 최소 이동 거리를 구해야한다.
            middle_idx = (temp_len // 2) - 1 if temp_len % 2 == 0 else temp_len // 2
            # 이 값은 temp_checker의 정렬된 x기준 or y기준으로 값을 정하고
            x_sorted = sorted(temp_checkers)
            y_sorted = sorted(temp_checkers, key=lambda checker: checker[1])
            x_value, y_value = x_sorted[middle_idx][0], y_sorted[middle_idx][1]
            # (x_value, y_value)로 temp_checkers들이 이동하는데 드는 비용을 구해야한다.
            total_cost = 0
            for temp_checker in temp_checkers:
                total_cost += (abs(temp_checker[0] - x_value) + abs(temp_checker[1] - y_value))
            min_total_cost = min(min_total_cost, total_cost)
        answer.append(min_total_cost)
    print(*answer)


def solve():
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    checkers = [tuple(map(int, input().split())) for _ in range(N)]

    # 체커들이 가진 모든 x, y좌표를 후보로 만든다.
    x_candidates = sorted(set(x for x, _ in checkers))
    y_candidates = sorted(set(y for _, y in checkers))

    # 각 k(1~N)에 대한 답을 매우 큰 값으로 초기화
    INF = 10 ** 15
    answer = [INF] * N  # answer[k-1]이 "적어도 k개의 체커를 모을 때"의 최소 이동 횟수

    # 모든 (x_candidates, y_candidates) 후보 칸을 순회
    for xx in x_candidates:
        for yy in y_candidates:
            # 이 칸으로 각 체커를 이동시킬 때 드는 비용
            costs = [abs(x - xx) + abs(y - yy) for x, y in checkers]
            costs.sort()

            # costs의 앞에서 k개를 합하면 "그 칸에 적어도 k개를 모으는 비용"
            s = 0
            for k in range(N):
                s += costs[k]  # k번째까지 누적
                # k+1개 모을 때 비용 => answer[k]와 비교 갱신
                if s < answer[k]:
                    answer[k] = s

    # k=1~N까지 답을 출력
    print(*answer)


solution()