from collections import deque
import sys

def solution():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split())) # 0이면 큐 1이면 스택
    B = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().split()))
    queuestack = deque()
    for i in range(N):
        if A[i] == 0:
            queuestack.append(B[i])
    answer = []
    for n in C:
        queuestack.appendleft(n)
        answer.append(queuestack.pop())
    print(" ".join(map(str, answer)))

solution()
# 아하... 시간초과가 걸려버렸네... 하긴 C에서 최대 10만 append에서 최대 10만... 최악이군..
# 자료구조안에 1개밖에 안들어있는데 너무 불필요한것을 했네... 그냥 다 연결시켜?