def solution():
    a, b, n, w = map(int, input().split())
    
    # 양은 x 염소는 y
    found = False
    answer = 0
    for x in range(1, n):
        y = n - x
        if not (0 < y < n):
            continue
        consumption_amount = x * a + y * b
        if consumption_amount == w:
            if found == False:
                answer = f"{x} {y}"
                found = True
            else:
                answer = -1
                break
    if found == False:
        print(-1)
    else:
        print(answer)

solution()