def solution():
    N, M, K = map(int, input().split())
    # 쌍은 무조건 2명과 1명으로 이루어져야하고... 이것을 최대한 많이 만드는 방법은?
    # N에서 몇명 M에서 몇명을 빼서 그게 K명이 되어야한다.
    
    ans = 0
    for w in range(N, -1, -1):
        for m in range(M, -1, -1):
            intern =  N - w + M - m
            if intern != K:
                continue
            # 이제 여자 w명 남자 m명에서 팀을 몇개 만들 수 있지? 그 최대 값을 찾아야한다.
            ans = max(ans, min(w // 2, m))
            
    print(ans)

solution()