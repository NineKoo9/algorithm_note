def solution():
    def calc_gcd(a, b):
        # a 와 b의 나머지 r이라면 a와 b의 최대 공약수는 b와 r의 최대 공약수와 같다.
        if b == 0:
            return a
        return calc_gcd(b, a % b)
    
    
    M, N = map(int, input().split(":"))
    
    gcd = calc_gcd(max(M, N), min(M, N))
    
    print(":".join([str(M // gcd), str(N // gcd)]))
    

solution()