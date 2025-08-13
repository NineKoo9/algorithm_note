def solution():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    prefix_sum = [0] * N
    prefix_sum[0] = A[0]
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]

    cnt = {0: 1}
    answer = 0
    for cur in prefix_sum:  # 문제를 정렬된 두 수의 차가 k인 경우의 수를 찾는 것으로 가도 되겠다.
        # 내가 무엇을 찾아야할지 무엇을 기억해야할지 잘 유의하자.
        need = cur - K # 현재 prefix sum cur 가 나왔을 때 이전에 cur-K 가 몇 번 등장했는지 더하면 됨
        # answer += cnt.get(need, 0)
        # cnt[cur] = cnt.get(cur, 0) + 1
        if need in cnt:
            answer += cnt[need]
        if cur in cnt:
            cnt[cur] += 1
        elif cur not in cnt:
            cnt[cur] = 1
    print(answer)
    
    
#밑의 풀이는 잘못되었다. 솔류션1이 올바르다
def solution2():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 부분합이 k인 녀석들의 갯수?
    
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
    
    need_cnt = {}
    ans = 0
    for r in range(N):
        prev = K + prefix_sum[r + 1]  # 이 값이 이전에 나타난적 있어야한다. 아....이거 식이 잘못되었네;; prev - prefix_sum[r+1] = K 이러면 완전 반대잖아...
        cur = prefix_sum[r + 1]  # 이 값은 이전에 나타난 값과 비교를 위해 필요하다.
        if prev in need_cnt:
            ans += need_cnt[prev]
        
        if cur + K in need_cnt:
            need_cnt[cur + K] += 1
        elif cur + K not in need_cnt:
            need_cnt[cur + K] = 1
            
    print(ans)
    # 이제부터 부분합을 구해야하는데...
    # 부분합을 어떻게 구할까?
    # 경우에따라서는 못보고 지나치는 것이 있을수있다. 그 값이 0일 수 있기에.
    # 이야... 최적화 기법 지린다.
    # prefix_sum[r + 1] - prefix_sum[l] = K
    # prefix_sum[r + 1] = K + prefix_sum[l] and l < r 이니까... 한반만 반복해도 충분하다.
    

solution2()