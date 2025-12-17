def solution():
    N = int(input())
    arrays = list(map(int, input().split()))
    pre_end = int(1e9)
    # 가장 긴 증가하는 수열들을 나타내는 인덱스를 활용해볼까?
    dp = [0] * N
    pre_table = [i for i in range(N)]
    dp[0] = 1
    if N == 1:
        print(1)
        print(arrays[0])
    else:
        for i in range(1, N):
            for j in range(i):
                if arrays[i] > arrays[j]:
                    # 이런식으로 간다면 2차 dp 가 필요한가?
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pre_table[i] = j
                else:
                    # 작은 경우는 어떻게 해야하지?
                    if dp[i] < 1:
                        dp[i] = 1
                        pre_table[i] = i
        # 이제부터 경로를 복원한다.
        max_value = max(dp)
        index = dp.index(max_value) # 처음에 이 값은 5가 될 것이다.
        path = []
        while pre_table[index] != index:
            pre_node = arrays[index]
            path.append(pre_node)
            index = pre_table[index]
        path.append(arrays[index])
        print(max_value)
        print(" ".join(map(str, path[::-1])))


def solution2():
    # 수열을 다 저장하면 될까..?
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[A[i]] for i in range(N)]
    if N == 1:
        print(1)
        print(A[0])
        return

    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j].copy() + [A[i]], key=lambda lst: len(lst))

    dp.sort(key=lambda lst: -len(lst))
    print(len(dp[0]))
    print(*dp[0])
# 엥 예전에 굳이 왜 경로복원 방법을 선택했지...?

solution2()