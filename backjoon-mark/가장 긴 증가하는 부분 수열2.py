def solution():
    def get_similar_num_index(num) -> int:
        # num 보다 조금 더 큰녀석을 찾는다...
        s = 0
        e = len(lis) -1
        while s < e:
            m = (s + e) // 2
            if num <= lis[m]:
                e = m
            else:
                s = m + 1 # 이 부분이 중요하다. 
        return e # 반환값이 e 인 것도 중요하다.
    
    
    N = int(input())
    arrays = list(map(int, input().split()))
    lis = [arrays[0]]
    for num in arrays[1:]:
        if num > lis[-1]:
            lis.append(num)
        else:
            # 작다면... num과 가장 차이가 안나면서 더 큰 원소를 찾는다?
            idx = get_similar_num_index(num)
            lis[idx] = num
    print(len(lis))


def solution2():
    def find_greater_idx(n):
        s = -1
        e = len(lis)
        while s + 1 < e:
            m = (s + e) // 2
            if lis[m] <= n:
                s = m
            else:
                e = m
        return e

    N = int(input())
    array = list(map(int, input().split()))
    lis = [array[0]]
    # 가장 긴 증가하는 수열을 찾아야한다.
    if N == 1:
        print(1)
        return
    for i in range(1, N):
        if lis[-1] < array[i]:
            lis.append(array[i])
        else: # 만약에 같거나 더 작다면...? 어떤 값과 바꿔치기해서... 증가하는 수열로 만들면 되게 좋겠다. 그러면 누구랑 바꿀까?
            idx = find_greater_idx(array[i])
            lis[idx] = array[i]

    print(len(lis))

def solution3():
    def binary_search_lower_bound(lst, num):
        lower = len(lst)
        start = 0
        end = len(lst) - 1
        while start <= end:
            mid = (start + end) // 2
            if lst[mid] >= num:
                lower = mid
                end = mid - 1
            else: # lst[mid] < num
                start = mid + 1
        return lower
    
    N = int(input())
    A = list(map(int, input().split()))
    
    stack = []
    for i in range(N):
        # 현재 stack에서 A[i]가 들어갈 위치를 찾는다.
        idx = binary_search_lower_bound(stack, A[i])
        if idx == len(stack):
            stack.append(A[i])
        else:
            stack[idx] = A[i]
            
    print(len(stack))

solution3()
# 자... 구현은 얼핏하긴했는데... 논리적인 이유부터 찾아보자