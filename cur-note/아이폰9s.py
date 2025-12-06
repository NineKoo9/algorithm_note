def solution():
    N = int(input())
    B = [int(input()) for _ in range(N)]
    
    set_B = set(B)
    # 단순히 브루트포스로 간단면...
    max_len = 0
    for target_to_remove in set_B:
        prev = -1
        cur_len = 0
        for i in range(N):
            # 제거되야할 숫자라면 그냥 건너뛴다.
            if B[i] == target_to_remove:
                continue
            
            if prev != -1 and B[i] != prev:
                max_len = max(max_len, cur_len)
                prev = B[i]
                cur_len = 1
                continue
            prev = B[i]
            cur_len += 1
        max_len = max(max_len, cur_len)
    print(max_len)
            
solution()