def solution():
    import sys

    input = sys.stdin.readline

    n = int(input())
    liquids = list(map(int, input().split()))

    left_idx = 0
    right_idx = n - 1

    ans = abs(liquids[left_idx] + liquids[right_idx])
    ans_left = left_idx
    ans_right = right_idx

    while left_idx < right_idx:  # left_idx와 right_idx는 만나면 안된다
        tmp = liquids[left_idx] + liquids[right_idx]

        if abs(tmp) < ans:
            ans_left = left_idx
            ans_right = right_idx
            ans = abs(tmp)

            if ans == 0:
                break

        if tmp < 0:
            left_idx += 1

        else:
            right_idx -= 1

    print(liquids[ans_left], liquids[ans_right])

    pass


def solution2():
    N = int(input())
    liquids = list(map(int, input().split()))
    
    s = 0
    e = N - 1
    min_diff = int(1e10)  # 범위값을 보다보니... 1e9을 하면 더한 값을 넘을 수 있음을 파악했다.!
    answer = []
    while s < e:
        l1, l2 = liquids[s], liquids[e]
        k = l1 + l2
        
        if k == 0:
            print(l1, l2)
            exit()
            
        # 일단 기존의 값과 비교할 필요가 있다. 일단 절댓값이 더 작다면 갱신해야할 필요가 있다.
        if abs(k) < min_diff:
            min_diff = abs(k)
            answer = [l1, l2]
        if k < 0:  # 이 다음은 커져야한다.
            s += 1
        else: # k > 0 이면 그 다음은 작아져야 한다.
            e -= 1
    print(*answer)
    
solution2()