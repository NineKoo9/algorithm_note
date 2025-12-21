def solution():
    # 병합 정렬(Merge Sort)의 시간 복잡도는 **(깊이) $\times$ (각 단계에서의 연산량)**으로 계산
    def div_and_conq(start, end, k):
        print(start, end)
        if end - start == 1:
            return [nums[start]]

        # 여기서 최종적으로 k명의 사람이 left, right을 정렬한다.
        left = div_and_conq(start, (start + end) // 2, k * 2)
        right = div_and_conq((start + end) // 2, end, k * 2)
        
        if k * 2 == K:
            print(*(left + right))
            exit()
            
        result = sorted(left + right)
        
        return result
            
    N = int(input())
    nums = list(map(int, input().split()))
    K = int(input())
    
    div_and_conq(0, N, 1)

# by 재미니
def solution2():
    N = int(input())
    nums = list(map(int, input().split()))
    K = int(input())
    
    # 1. 한 사람이 담당해야 할 개수 (step) 구하기
    step = N // K
    
    answer = []
    
    # 2. 리스트를 step만큼 건너뛰면서 잘라서 정렬하기
    for i in range(0, N, step):
        # i부터 i+step까지 잘라서(slicing) 정렬
        part = sorted(nums[i : i + step])
        answer += part # 정렬된 조각을 결과 리스트에 붙이기
        
    # 출력 (리스트의 요소들을 공백으로 구분해서 출력)
    print(*answer)

# 재귀 함수를 이용한다면 이렇게 하는 것이 더 맞다.
def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    K = int(input())

    def div_and_conq(start, end, k):
        # 1. 목표 단계인 K명에 도달했으면, 현재 구간을 정렬해서 반환
        if k == K:
            return sorted(nums[start:end])
        
        # 2. 아직 목표 단계가 아니면 계속 분할 (k를 2배로 늘림)
        mid = (start + end) // 2
        left = div_and_conq(start, mid, k * 2)
        right = div_and_conq(mid, end, k * 2)
        
        # 3. 하위 단계에서 정렬된 조각들을 받아서 단순히 합침 (여기서는 정렬 X)
        return left + right

    # 처음에 1명이 시작 (start=0, end=N, k=1)
    result = div_and_conq(0, N, 1)
    print(*result)

solution()