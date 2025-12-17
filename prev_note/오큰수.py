def solution():
    from collections import deque

    N = int(input())  # 1~1e6
    arr = list(map(int, input().split()))  # 각 원소의 크기도 100만 까지
    answer = [-1] * (N)
    stack = deque()
    stack.append(0)
    for idx in range(1, N):
        while stack and arr[idx] > arr[stack[-1]]:
            answer[stack.pop()] = arr[idx]
        stack.append(idx)

    for i in answer:
        print(i, end=" ")


# 오큰수를 어떻게 구할까?
# 시간 초과가 발생했다.
# 어떻게 해결할까? 제한시간은 1초이며 100만의 길이에 겨우 10만 곱하기가 가능한 처지가
# 정렬 알고리즘을 쓰면서 바뀌기만 하면 기록할까?
# 원소 하나하나에 대해서 확인하며 오른쪽 녀석들을 살펴보는것은 시간이 안된다.

# 이 방식의 시간 복잡도를 어떻게 계산해야 할까
# 어쨋든 이러한 인덱스를 stack에 넣는것은 시간을 크게 줄일 수 잇구나


def solution2():
    n = int(input())
    arr = list(map(int, input().split()))
    answer = [-1] * n
    # 반복문? 중복되는 것이 존재한다.
    """
        for idx, ch in enumerate(arr):
            # 스택을 활용하는 것이 아니라면,
            for r_ch in arr[idx:]:
                if r_ch > ch:
                    answer.append(r_ch)
    """
    # stack을 활용하여 리버스로 탐색하는것도 시도해보자
    stack = []
    stack.append(0)
    for i in range(1, n):
        while stack and arr[stack[-1]] < arr[i]:
            answer[stack.pop()] = arr[i]
        stack.append(i)

    print("answer: ", answer)
    # 이런 경우는 시간 복잡도를 n * (n/2)라고 볼수 있구나... (n/2)는 이중포문 안의 평균적인 값..?
    # 내가 이게 잘 안되는 것 같다. 처음에는 아무런게 없으니까 일정이상은 if나 while이 무시되며 for문이 돌아갈텐데 그걸 구조적으로 설계가 쉽지 않군

def solution4():
    N = int(input())
    A = list(map(int, input().split()))
    
    stack = []
    NGE = [-1 for _ in range(N)]
    for i in range(N):
        while stack and A[stack[-1]] < A[i]:
            prevIdx = stack.pop()
            NGE[prevIdx] = A[i]
        stack.append(i)
    print(*NGE)

solution4()
