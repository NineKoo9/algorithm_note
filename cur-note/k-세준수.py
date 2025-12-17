import sys

# 입력을 빠르게 받기 위한 설정 (백준 채점 시 권장)
input = sys.stdin.readline

# 1. N과 K 입력받기
N = int(input())
K = int(input())

# 2. 각 숫자의 '가장 큰 소인수'를 저장할 배열 (0으로 초기화)
# 인덱스 1부터 N까지 사용
maxFactor = [0] * (N + 1)

# 3. '응용된 에라토스테네스의 체' 실행
for i in range(2, N + 1):
    # i가 아직 처리되지 않았다면 (즉, maxFactor[i]가 0이라면)
    # i는 소수(prime)이거나, i의 가장 큰 소인수는 i 자신이다.
    if maxFactor[i] == 0:
        
        # i의 배수들(j)을 순회하며 '덮어쓰기'
        # (i*1, i*2, i*3, ...)
        for j in range(i, N + 1, i):
            # j의 가장 큰 소인수를 i로 갱신 (덮어쓰기)
            maxFactor[j] = i

# 4. K-세준수 개수 세기
answer_count = 0
for i in range(1, N + 1):
    # i의 가장 큰 소인수(maxFactor[i])가 K보다 작거나 같으면
    if maxFactor[i] <= K:
        answer_count += 1

# 5. 최종 결과 출력
print(answer_count)