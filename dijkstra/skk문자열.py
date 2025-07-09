def solution():
    S = list(input())
    l = len(S)
    prefix_count_s = [0] * l
    prefix_count_k = [0] * l
    for i in range(len(S)):
        ch = S[i]
        prefix_count_k[i] = prefix_count_k[i - 1] if i - 1 >= 0 else 0
        prefix_count_s[i] = prefix_count_s[i - 1] if i - 1 >= 0 else 0
        if ch == "S":
            prefix_count_s[i] = prefix_count_s[i] + 1
        elif ch == "K":
            prefix_count_k[i] = prefix_count_k[i] + 1

    # 슬라이딩 윈도우로 가보자.
    max_l = -1
    start = 0
    end = 0
    while 0 <= start <= end < l:
        s_count = prefix_count_s[end] - (prefix_count_s[start - 1] if start - 1 >= 0 else 0)
        k_count = prefix_count_k[end] - (prefix_count_k[start - 1] if start - 1 >= 0 else 0)
        if 2 * k_count == s_count:
            max_l = max(max_l, end - start + 1)
            end += 1
        elif 2 * k_count > s_count:
            pass
        elif 2 * k_count < s_count:
            pass


# gpt가 작성한 풀이임.
import sys
input = sys.stdin.readline

def solution2():
    S = input().strip()
    l = len(S)

    # 1) prefix_count_s[i] = S[0..i]까지 S 개수
    #    prefix_count_k[i] = S[0..i]까지 K 개수
    prefix_count_s = [0] * l
    prefix_count_k = [0] * l
    for i, ch in enumerate(S):
        if i > 0:
            prefix_count_s[i] = prefix_count_s[i-1]
            prefix_count_k[i] = prefix_count_k[i-1]
        if ch == 'S':
            prefix_count_s[i] += 1
        elif ch == 'K':
            prefix_count_k[i] += 1

    # 2) diff = k_count - 2*s_count 의 최초 등장 인덱스와
    #    그때까지의 s_count 를 저장할 딕셔너리
    #    diff == 0 은 “아무것도 고르지 않은 상태”로, j = -1에 있다고 가정
    first_index_for_diff = {0: -1}
    first_s_for_diff     = {0:  0}

    best_len = -1

    # 3) 각 i 위치에서 diff를 계산하고
    #    처음 나온 diff면 기록, 아니면 최초 위치와 비교해서 구간 길이를 갱신
    for i in range(l):
        s_count = prefix_count_s[i]
        k_count = prefix_count_k[i]
        diff = k_count - 2 * s_count

        if diff not in first_index_for_diff:
            # 처음 나온 diff → 저장
            first_index_for_diff[diff] = i
            first_s_for_diff[diff]     = s_count
        else:
            # 이미 나온 diff라면 [j+1 .. i] 구간이 K=2S 조건 만족
            j      = first_index_for_diff[diff]
            prev_s = first_s_for_diff[diff]
            # S가 최소 1회 이상 포함됐는지 확인
            if s_count - prev_s > 0:
                length = i - j
                if length > best_len:
                    best_len = length

    print(best_len)

# 백준에서 누군가의 풀이...
def solution4():
    S = input()

    N = len(S)
    arr = [0]*N
    for i in range(N):
        arr[i] += arr[i-1]
        if S[i] == 'S': arr[i] += 2
        elif S[i] == 'K': arr[i] -= 1

    idx = {0:-1}
    for i in range(N):
        if arr[i] not in idx:
            idx[arr[i]] = i

    result = -1
    p = -1
    for i in range(N):
        j = idx[arr[i]]
        if j < p: result = max(result,i-j)
        if S[i] in 'SK': p = i
    print(result)

# 백준에서 누군가의 풀이...
def solution5():
    import sys
    from collections import defaultdict

    string = sys.stdin.readline().rstrip()
    s = 0

    visited = dict()
    changed = defaultdict(bool)
    answer = -1
    visited[0] = -1
    for i, c in enumerate(string):
        if c == 'S':
            changed[s] = True
            s += 2
        elif c == 'K':
            changed[s] = True
            s -= 1
        if s not in visited: visited[s] = i
        elif changed[s]: answer = max(answer, i - visited[s])

    print(answer)

# 식을 세우는 것 까지는 그렇다쳐도... diff[r + 1] - diff[l] 이걸 세운다쳐도 그 이후 디테일한 부분을 처리하기에는 쉽지 않다.
def solution3():
    S = input().rstrip()
    
    prefix_s_count = [0] * (len(S) + 1)
    prefix_k_count = [0] * (len(S) + 1)
    for i in range(1, len(S) + 1):
        prefix_s_count[i] = prefix_s_count[i - 1] + (1 if S[i - 1] == "S" else 0)
        prefix_k_count[i] = prefix_k_count[i - 1] + (1 if S[i - 1] == "K" else 0)
    
    # 이제부터 가장 긴 skk 문자열을 출력해야한다.
    diff = {0: 0}
    ans = -1
    for i in range(1, len(S) + 1):
        diff_value = 2 * prefix_s_count[i] - prefix_k_count[i]  # 이 값이 0인 경우가 문제가 되네?
        
        if diff_value not in diff:
            diff[diff_value] = i
        
        # 이제 처음 값을 기준으로 원래의 값과 비교한다.
        l = diff[diff_value]
        r = i
        # 반드시 1개 이상있어야한다는 조건을 따지자.
        cntS = prefix_s_count[r] - prefix_s_count[l]
        cntK = prefix_k_count[r] - prefix_k_count[l]
        if cntS < 1 or cntK < 1:
            continue
        ans = max(ans, r - l)
        
        
    print(ans)
        

solution3()
