def solution():
    def is_hansu(N):
        lst = [int(ch) for ch in str(N)]
        # lst의 각 원소가 등차수열을 이루는지 확인해야한다.
        if len(lst) == 1:
            return True
        a = lst[0]
        d = lst[1] - lst[0]
        
        i = 0
        for n in lst:
            if n != a + d * i:
                return False
            i += 1
        return True
            
    N = int(input())    
    hansu_count = 0
    for i in range(1, N + 1):
        if is_hansu(i):
            hansu_count += 1
            
    print(hansu_count)

solution()