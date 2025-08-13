import bisect

# 아하... 인덱스 값을 길이로하고.. 값을 A[i]로 두었구나?
# 길이라는 것을 변수화해서.. 인덱스로 활용했다라..
# arrays[i]가 이전 값보다 작다면... 어디에 붙어야 하는데 그것을 어떻게 찾을까?
# 모든 앞의 녀석들을 탐험할 수 없다. 다만... 현재 값보다 작은 녀석들을 찾아야한다.
# 그리고 그 값이 가지고 있는 최대부분수열 길이라는 정보도. 즉 2개의 정보가 필요하다. 현재 앞에 있는 녀석들 근데 그 중에서 어떤 수열의 끝이 되는 녀석들만, 그리고 그 녀석들이 가지고 있는 최대부분수열의 길이
# 이 2개를 포함할 정보는 tails[]로 구현했구나?
# 애초에 이렇게 가면 dp가 필요한 문제도 아니네
# 이런 코드를 구성할 수 있다는 것이 생각하기가 쉽지 않다.
# 내가 필요로하는 정보를 모두 담고 있고 갱신하기도 편하다.
def solution():
    def get_index(num):
        idx = bisect.bisect_left(tails, num)
        return idx
    
    N = int(input())
    arrays = list(map(int, input().split()))
    tails = [arrays[0]]
    for i in range(1, N):
        if tails[-1] < arrays[i]:
            tails.append(arrays[i])
        else:
            idx = get_index(arrays[i])
            tails[idx] = arrays[i]
    print(len(tails))


# 이 풀이는 잘못된 풀이다.
def solution2():
    N = int(input())
    A = list(map(int, input().split()))

    def search(v):
        start = 0
        end = len(prev_stack)
        while start + 1 < end:
            mid = (start + end) // 2

            if prev_stack[mid] < v:
                start = mid
            else:
                end = mid

        idx = longest_by_value_dp[prev_stack[end]]
        return idx

    prev_stack = []
    longest_by_value_dp = [0] * 1000001
    longest_by_idx_dp = [0] * 1000001

    for i in range(N):
        value = A[i]
        prev_idx = search(value) # 이 함수는 어떤 녀석 뒤에 이어갈지를 반환하는 것이다.
        longest_by_idx_dp[i] = max(longest_by_idx_dp[i], longest_by_idx_dp[prev_idx] + 1)

        # 이제 탐색한 value는 stack에 넣는다. 단 단조로운 감소가 되도록.
        while prev_stack[-1] < value:
            prev_stack.pop()
        prev_stack.append(value)
        longest_by_value_dp[value] = longest_by_idx_dp[i]

solution2()