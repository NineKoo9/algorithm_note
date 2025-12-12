import math

# 1. 입력 받기
N, M, K = map(int, input().split())

# 2. 전체 경우의 수 구하기: N개 중 M개를 뽑는 경우 (nCm)
total_cases = math.comb(N, M)

# 3. 당첨되는 경우의 수 구하기 (적어도 K개 이상 일치)
winning_cases = 0

# i는 일치하는 숫자의 개수 (K개부터 M개까지 반복)
for i in range(K, M + 1):
    # 당첨 번호 M개 중에서 i개를 뽑는 경우의 수
    chosen_winning = math.comb(M, i)
    
    # 나머지(꽝) 번호 N-M개 중에서 나머지 M-i개를 뽑는 경우의 수
    chosen_losing = math.comb(N - M, M - i)
    
    # 두 경우를 곱해서 더함 (동시에 일어나는 사건이므로 곱셈)
    winning_cases += chosen_winning * chosen_losing

# 4. 확률 계산 및 출력
if total_cases == 0:
    print(0.0)
else:
    print(winning_cases / total_cases)