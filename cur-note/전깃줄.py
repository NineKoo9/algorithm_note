def solution():
    # 현재 상태가 엉켜있는지 안 엉켜있는지 확인할수있는 함수가 필요하지 않을까? 이건 결국 필요없었네
    def check(lines):
        sorted_lines = sorted(lines)
        b_point = sorted_lines[0][1]
        for _, n_b_point in sorted_lines[1:]:
            if n_b_point < b_point:
                return False
            b_point = n_b_point
        return True
            
    
    
    N = int(input())
    N_lines = [tuple(map(int, input().split())) for _ in range(N)]
    N_lines.sort()
    INF = int(1e9)
    dp = [[-INF, -INF] for _ in range(N)]
    dp[0][0] = 0
    dp[0][1] = 1
    for i in range(1, N):
        b_point = N_lines[i][1]
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) # 현재 줄을 설치하지 않는다면 전까지 설치된 갯수를 인정한다. 그 전 녀석이 설치되엇을수도있고 아닐수도 있지만 
        for j in range(i):
            prev_b_point = N_lines[j][1]
            if prev_b_point < b_point:
                dp[i][1] = max(dp[i][1], dp[j][1] + 1)
            else:
                dp[i][1] = max(dp[i][1], 1)
    print(dp)
    max_value = -INF
    for i in range(N):
        max_value = max(dp[i][0], dp[i][1])    
    print(N - max_value)

def solution2():
    N = int(input())
    electric_lines = [tuple(map(int, input().split())) for _ in range(N)]
    electric_lines.sort()
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if electric_lines[i][1] > electric_lines[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(N - max(dp))

def solution3():
    N = int(input())  # 100개 이하
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    lines.sort()
    array = [b for a, b in lines]
    # 이제부터 array에서 가장 긴 증가하는 부분 수열을 구해야한다.

    # 우선 100밖에 안되지만... 엄청 큰 경우를 가정해보자.
    # 초기 값을 무엇으로 하지?
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(N - max(dp))

# 만약 N이 100만이라 가정해보자. 그렇다면 훨씬 더 최적화를 해야한다.
# 근데 이렇게 해도 시간은 똑같구만..
def solution4():
    from bisect import bisect_right

    N = int(input())  # 100개 이하
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    lines.sort()
    array = [b for a, b in lines]
    # 이제부터 array에서 가장 긴 증가하는 부분 수열을 구해야한다.

    # 우선 100밖에 안되지만... 엄청 큰 경우를 가정해보자.
    # 문제는 앞 녀석을 매번 탐색한다는 것이다.
    stack = []
    for i in range(N):
        num = array[i]
        insert_idx = bisect_right(stack, num)
        if insert_idx == len(stack):
            stack.append(num)
        else:
            stack[insert_idx] = num
    print(N - len(stack))

solution4()