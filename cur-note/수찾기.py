def solution():
    def check(n):
        # n이 array 안에 존재하는지 안하는지 체크하는 문제다
        # 10만개의 데이터에 대해서 10만개의 배열에 체크해 나가는 것이고 그냥 단순 계산하면 10^12 로 엄청난 시간 복잡도를 가진다
        # 이진탐색을 통해 체크해 보자. 
        s = 0
        e = N - 1
        while s <= e : # s 와 e가 같다면 mid 도 같은 값이 될 것이다.
            mid = (s + e) // 2
            if n < Array[mid]: # mid는 내림이 된 상태인데.. n이 그 보다 작다면..n의 범위는 mid에 해당하는 index의 녀석에는 포함안될 것이고.. 그보다 작은 인덱스 녀석은 포함할 수 있다.
                e = mid - 1
            elif n > Array[mid]:
                s = mid + 1
            else: # n == Array[mid]
                return True
        return False
    
    def check2(n):
        import bisect
        
        r = bisect.bisect_left(Array, n) # 만약에 n이 Array 안에 존재한다면... r이라는 인덱스에 해당하는 값이 n과 일치하겠지?
        if r < N and n == Array[r]:
            return True
        else:
            return False
    
    
    N = int(input())
    Array = list(map(int, input().split()))
    Array.sort()
    M = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        if check(num):
            print(1)            
        else :
            print(0)
    pass

solution()