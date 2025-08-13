def solution():
    N, K = map(int, input().split())
    # N의 약수둘 중에서 K번째로 작은 수를 구해야
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count += 1
            if count == K:
                print(i)
                break
    if count < K:
        print("0")

solution()
