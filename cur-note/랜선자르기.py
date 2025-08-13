def solution():
    def count_available_lines(length):
        count = 0
        for line in lines:
            count += (line // length)
        return count
    
    K, N = map(int, input().split()) # 가지고 있는 K개의 랜선 (10000이하), 필요한 N개의 랜선 (100만 이하) K <= N
    lines = [int(input()) for _ in range(K)] # line 하나의 길이는 최대 2^31.. 어마어마한 길이다
    lines.sort()
    max_len = lines[-1] + 1 # 잠시만... 여기가 문제 같은데?
    min_len = 1
    while min_len + 1 < max_len: # 이렇게 조건을 잡으면 반드시 min < mid < max 가 이루어진다.
        mid_len = (min_len + max_len) // 2
        # mid의 길이로 잘랐을때 만들수 있는 선의 갯수를 구해야하고 그에따라서 이분탐색을 해나가야한다.
        num_of_lines = count_available_lines(mid_len)
        if num_of_lines < N:
            # 만들 수 있는 라인의 수가 필요한 N보다 작다면... 길이를 더 줄여나가야 한다.
            max_len = mid_len # mid보다 크다면? N개 자체를 만들수 없을것이다.
        elif num_of_lines >= N: # num_of_lines > N:
            # 만들 수 있는 라인의 갯수가 N개보다 많다면 최대한 mid을 길게 가져갈려고 하자.
            min_len = mid_len  # 어짜피 mid 부분은 N개 보다 크니까 mid 보다 조금 더 큰 부분을 탐색하자
           
    print(min_len)
    
    
solution()

# 문제를 살짝 바꿔서, 개수가 N보다 작게 되는 최소 길이를 구한다고 하겠습니다. 거기서 1을 빼면 원래 문제의 답이 됩니다.

def solution2():
    def check(m: int) -> int: # 만들 수 있는 랜선의 갯수라하자.
        count = 0
        for l in len_lst:
            count += l // m
        return count

    K, N = map(int, input().split())
    len_lst = [int(input()) for _ in range(K)]
    s = 1
    e = int(3e9)
    while s + 1 < e:
        mid = (s + e) // 2
        if check(mid) >= N:
            s = mid
        else:
            e = mid

    pass
