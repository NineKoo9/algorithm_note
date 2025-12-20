def solution():
    n, m = map(int, input().split())
    # 리프란 것은 결국 하나만 연결된 노드가 몇개이냐 로 가면 되겟다.
    
    j = 0
    for i in range(1, n):
        print(j, i)
        if j <= n - m - 1:
            j += 1
        
solution()