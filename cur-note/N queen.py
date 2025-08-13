# n = int(input())
from scipy.special import factorial


# ans = 0
# row = [0] * n

# def is_promising(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#             return False
    
#     return True

# def n_queens(x):
#     global ans
#     if x == n:
#         ans += 1
#         return

#     else:
#         for i in range(n):
#             # [x, i]에 퀸을 놓겠다. 이걸 이렇게 표현할 수 있다니...
#             # 아니 근데.. 여기 이렇게 놓겠다가 되었으면.. 롤백도 해야하지 않나? 아... 위협을 받는다면 계속해서 i 값으로 업데이트 되는 구나?
#             row[x] = i
#             if is_promising(x):
#                 n_queens(x+1)

# n_queens(0)
# print(ans)




# N = int(input())
# count = 0
# row = [0] * N
#
# def is_under_attack(y):
#     for prev_y in range(y): # x 값보다 작은 y값만 보면 된다.
#         # 다른 row 에 x의 값을 가지고 있다면 안되고.. 대각선도 안됨
#         if row[prev_y] == row[y] or y - prev_y == abs(row[prev_y] - row[y]):
#             return True
#     return False
#
# def n_queens(y):
#     global count
#
#     if y == N: # 한발짝 더 나아갔다가 리턴하는 것이다..
#         count += 1
#         return # 여기서 더이상 탐색하지 말아야 한다...
#
#     for x in range(N):
#         row[y] = x
#         if is_under_attack(y):
#             continue
#         n_queens(y + 1)
#
# n_queens(0)
# print(count)


# 이 방식은 시간초과가 나타난다...
# def solution2():
#     def is_ok(y, x):
#         # 자 여기서 괜찮은지 어케 체크할까? 상하좌우대각선 체크해야한다.
#         for prev_y in range(y):
#             if Map[prev_y][x] == 1:
#                 return False
#             for prev_x in range(len(Map)):
#                 if Map[prev_y][prev_x] == 1 and abs(x - prev_x) == abs(y - prev_y):
#                     return False
#         return True
#
#     def dfs(y):
#         if y == N:
#             count.append(1)
#             return
#
#         for x in range(N):
#             Map[y][x] = 1
#             if is_ok(y, x):
#                 dfs(y + 1)
#             Map[y][x] = 0
#
#     N = int(input())
#     count = []
#     Map = [[0] * N for _ in range(N)]
#     dfs(0)
#     print(sum(count))
#
# def solution3():
#     def is_ok(y, x):
#         # 자 여기서 괜찮은지 어케 체크할까? 상하좌우대각선 체크해야한다.
#         for prev_y in range(y):
#             if Row[prev_y] == x:
#                 return False
#             # 자 이제 대각선을 체크해야지?
#             if Row[prev_y] != -1 and abs(Row[prev_y] - x) == abs(y - prev_y):
#                 return False
#         return True
#
#     def dfs(y):
#         if y == N:
#             count.append(1)
#             return
#
#         for x in range(N):
#             Row[y] = x
#             if is_ok(y, x):
#                 dfs(y + 1)
#             Row[y] = -1
#
#     N = int(input())
#     count = []
#     Row = [-1] * N # 차원을 하나 줄여서...
#     dfs(0)
#     print(sum(count))
#
# def solution4():
#     def is_ok(y, x):
#         # 여기서 y, x가 가능한가?
#         for prev_y in range(y):
#             if dp[prev_y] == x or abs(y - prev_y) == abs(x - dp[prev_y]):
#                 return False
#         return True
#
#     def dfs(start_y):
#         if start_y == N:  # start는 x값으로 점점 깊어진다.
#             count.append(1)
#             return
#
#         for x in range(N):
#             if is_ok(start_y, x):
#                 dp[start_y] = x
#                 dfs(start_y + 1)
#
#     N = int(input())  # N이 15가 최대라면 이 경우의 최악의 시간복자도는 15팩토리얼이다... 그렇지만 가지치기를?
#     dp = [-1] * N  # dp[x] = y
#     count = []
#     dfs(0)
#     print(sum(count))

import sys

input = sys.stdin.readline

def is_ok(y, x):
    for prev_y in range(y):
        if dp[prev_y] == x or abs(y - prev_y) == abs(x - dp[prev_y]):
            return False
    return True

def dfs(start_y):
    global count
    if start_y == N:  # start는 x값으로 점점 깊어진다.
        count += 1
        return

    for x in range(N):
        if is_ok(start_y, x):
            dp[start_y] = x
            dfs(start_y + 1)

N = int(input())  # N이 15가 최대라면 이 경우의 최악의 시간복자도는 15팩토리얼이다... 그렇지만 가지치기를?
dp = [-1] * N  # dp[x] = y
count = 0
dfs(0)
print(count)

