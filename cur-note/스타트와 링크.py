# 이 방식은 메모리 초과가 발생하는구나... 메모리초과를 막기위해 제너레이터를 썼지만...
# 이제는 시간초과에 걸린다...
# 구글에 dfs로 푼 코드를 봤는데 중복을 처리하지는 못하네...
import itertools

def solution():
    def get_team_combinations(p_lst):
        # 여기서 팀의 조합을 찾아야한다...
        combinations = list(itertools.combinations(p_lst, len(p_lst) // 2))
        combinations.sort()
        combinations_size = len(combinations)
        for i in range(combinations_size // 2):
            yield combinations[i], combinations[combinations_size - i - 1]  # 여기서 이렇게 짝이 맞춰진다는 것이 신기하네

    def get_power(team: list) -> int:
        power = 0
        combs = itertools.combinations(team, 2)
        for a, b in combs:
            power += S[a-1][b-1]
            power += S[b-1][a-1]
        return power

    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    players = [i for i in range(1, N + 1)]
    min_balance = int(1e9)
    for team_a, team_b in get_team_combinations(players):
        min_balance = min(min_balance, abs(get_power(team_a) - get_power(team_b)))
    print(min_balance)


def solution2():
    from itertools import combinations

    def get_power(team) -> int:
        # 팀은 최소 두명이다.
        result = 0
        for p1 in team:
            for p2 in team:
                if p1 == p2:
                    continue
                result += board[p1][p2]
        return result

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i, j in zip(board, zip(*board)):
        print(i, j)


    sum_stat = [sum(i) + sum(j) for i, j in zip(board, zip(*board))]
    nums = [i for i in range(N)]

    min_diff = int(1e9)
    for team_A in combinations(nums, N // 2):
        team_B = set(nums) - set(team_A)
        min_diff = min(min_diff, abs(get_power(team_A) - get_power(team_B)))

    print(min_diff)

# 이야... 이 풀이 대단하다.
def solution3():
    import sys
    from itertools import combinations
    N = int(sys.stdin.readline())
    stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    sum_stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]  # 대각선끼리 합
    allstat = sum(sum_stat) // 2  # 모든 값 합의 절반
    result = float('inf')
    for l in combinations(sum_stat, N // 2):  # 대각선 합에서 뽑은 2개 중에서
        result = min(result, abs(allstat - sum(l)))  # 모든 값의 절반 - 그 뽑은 2개 합의 차 = start팀 - link팀
    print(result)
solution2()

