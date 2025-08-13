def solution():
    def div_conq(y, x, size):
        if size == 1:
            return S[y][x]
        
        size = size // 2
        r1 = div_conq(y, x, size)
        r2 = div_conq(y, x + size, size)
        r3 = div_conq(y + size, x, size)
        r4 = div_conq(y + size, x + size, size)
        if len(r1) == 1 and r1 == r2 == r3 == r4:
            return r1
        # 서로 다르다면? 각자를 하나의 튜플로 전달해야 한다.
        return f"({r1}{r2}{r3}{r4})"
            
    N = int(input())
    S = [input() for _ in range(N)]
    # 최종 결과를 어떻게 표현해야할까의 고민이 있지만 문제를 풀어나가며 정해보자.
    result = div_conq(0, 0, N)
    print(result)
    
solution()
# 처음부터 모두 같은 경우는 어떻게 괄호안에 결과를 넣을까?
# 와.... 문자열 (0011) (0011) 도 같으면... 그냥 고대로 하나로 치환해버려서 문제가 발생했다...