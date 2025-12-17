def solution():
    N, M, K = map(int, input().split())
    
    # 배열의 최대 크기는 100만개이다.
    # K는 1이상 최대 10만이다.
    if N + M > K + 1:
        print("NO")
        exit()
    # 그렇다면 이제 되는 것 아무것이나 출력하자.
    print("YES")
    arr = [[i + j + 1 for j in range(M)] for i in range(N)]
    for row in arr:
        print(*row)

solution()